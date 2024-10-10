"""
Extract a dataset from a URL like Kaggle
or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests

def extract(url="https://raw.githubusercontent.com/Barabasi-Lab/GroceryDB/main/data/GroceryDB_IgFPro.csv", 
            file_path="data/GroceryDB_IgFPro.csv", timeout=10):
    """Extract a url to a file path"""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Check for HTTP request errors
        with open(file_path, 'wb') as f:
            f.write(response.content)
        return file_path
    except requests.exceptions.Timeout:
        print(f"Request timed out after {timeout} seconds")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return None
