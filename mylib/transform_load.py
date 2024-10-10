"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,
avg_FPro_products,avg_distance_root,ingred_normalization_term,
semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv
import os

# Load the csv file and insert into a new SQLite3 database
def load(dataset="/workspaces/Osama-sqlite-lab/data/GroceryDB_IgFPro.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    # Prints the current working directory
    print("Current working directory:", os.getcwd())

    # Open the CSV file and read its content
    try:
        with open(dataset, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            # Skip the header row if present
            header = next(reader, None)
            print(f"Header: {header}")

            # Establish a connection to the SQLite database
            with sqlite3.connect('GroceryDB.db') as conn:
                c = conn.cursor()
                c.execute("DROP TABLE IF EXISTS GroceryDB")
                c.execute("""CREATE TABLE GroceryDB (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            general_name TEXT,
                            count_products INTEGER,
                            ingred_FPro REAL,
                            avg_FPro_products REAL,
                            avg_distance_root REAL,
                            ingred_normalization_term REAL,
                            semantic_tree_name TEXT,
                            semantic_tree_node TEXT)""")

                # Insert data into the table
                for row in reader:
                    if len(row) == 8:  # Ensure the correct number of columns
                        c.execute("""INSERT INTO GroceryDB 
                                    (general_name, count_products, ingred_FPro,
                                     avg_FPro_products, avg_distance_root,
                                     ingred_normalization_term, semantic_tree_name,
                                     semantic_tree_node)
                                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", row)

                conn.commit()
                print("Data successfully loaded into GroceryDB")

        return "GroceryDB.db"
    
    except FileNotFoundError:
        print(f"File not found: {dataset}")
        return None
    
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None
    
    except ValueError as e:
        print(f"ValueError encountered: {e}")
        return None
    
    except OSError as e:
        print(f"OS error: {e}")
        return None
