# SQLite Project | Data Ingestion, Transformation, Querying, and CRUD Operations

This project demonstrates a robust data pipeline leveraging SQLite, which encompasses the processes of data ingestion, transformation, querying, and executing CRUD (Create, Read, Update, Delete) operations. The project is designed to support Continuous Integration and Continuous Deployment (CI/CD) pipelines, automating various database operations with every commit to the repository. Furthermore, it provides the capability to run queries through a command line interface (CLI), offering optional output to facilitate efficient data analysis and management.

## Key Features

- Import data from external sources into an SQLite database.
- Cleanse and transform data for insightful analysis.
- Execute SQL queries to derive data insights.
- Carry out CRUD operations on database entries.
- Automate data pipeline tasks with CI/CD integration.

## How to Use

### Running the Data Pipeline

To initiate the data pipeline, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Execute the data pipeline using the `main.py` script, optionally appending the `--query` flag on the command line as necessary.

### Running Queries

This project allows users to execute SQL queries and view the resulting data. You can include the `--query` flag followed by your SQL statement to display the query results in the output.

This command will execute your specified SQL query and show the corresponding results.

## CI/CD Integration

This project is set up with Continuous Integration and Continuous Deployment (CI/CD) pipelines. Upon each push to the repository, the following actions are automatically carried out:

1. Data is loaded into the SQLite database.
2. Data transformation and cleansing processes are conducted.
3. SQL queries are executed.
4. The output of these operations is logged.

The results of the operations, including any query results and CRUD actions, are automatically documented in an `output.txt` file for later reference.
