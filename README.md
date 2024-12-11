# Data Pipeline with Databricks | ETL and Data Management 
This project demonstrates the creation and execution of a data pipeline using Databricks. It includes data ingestion, transformation, and querying with support for Continuous Integration and Continuous Deployment (CI/CD). The pipeline is designed to load data from a source, process it, and store it in a specified sink, showcasing the seamless integration of Databricks with GitHub.

## Features
- Extract, transform, and load (ETL) data in Databricks.
- Perform CRUD operations using Databricks workflows.
- Configure CI/CD to automate pipeline execution and database updates.
- Enable SQL queries for analysis and data exploration.
- Manage workflow stages (Extract, Transform, Load, Query) using Databricks Jobs.

## Requirements
- Build a data pipeline using Databricks.
- Include at least one data source and one data sink.
- Implement a CI/CD pipeline for automation.

## 🛠️ Setup Instructions

### Cloning the Repository
1. Log into your Databricks workspace.
2. Navigate to the **Workspace** section and click on **Users**.
3. Locate your email ID and click on it.
4. Select **Create** in the top-right corner and choose **Git Folder**.
5. Paste the GitHub repository link and click **Create**.

### Setting up the Compute Cluster
1. Navigate to the **Compute** section in Databricks.
2. Click **Create** and select **Personal Compute**.
3. Configure the cluster settings appropriately.

### Installing Required Libraries
1. Open your personal compute cluster and navigate to the **Libraries** tab.
2. Install libraries via PyPI
3. Follow the prompts to complete the installation.

### Linking GitHub to Databricks
1. Go to **Account Settings** (profile icon in the top-right corner).
2. Navigate to **Linked Accounts**.
3. Use a **Personal Access Token** to link your GitHub account.

## 🚀 ETL Pipeline

### Setting up the Pipeline in Databricks
1. Navigate to the **Workflows** section in Databricks.
2. Click **Create Job** to set up individual tasks for each ETL stage.

#### Task 1 - Extract
1. Create a new task named **"Extract"**.
2. Set the type to **Python Script**.
3. Use the path to your `extract.py` file in the repository.
4. Assign the compute cluster to this task.
5. Click **Create Task**.

#### Task 2 - Transform and Load
1. Add a task named **"Transform_Load"**.
2. Use the same configuration as the **Extract** task.
3. Set **Depends On** to **Extract** to ensure sequential execution.

#### Task 3 - Query
1. Add a task named **"Query"**.
2. Use the same configuration as the **Transform_Load** task.
3. Set **Depends On** to **Transform_Load**.

## Usage

### Running the Pipeline
1. After configuring the workflow, navigate to **Workflows** and trigger the pipeline.
2. Monitor the execution of each task to ensure sequential processing.

### Executing Queries
- Use the `query.py` script to run SQL queries.
- For example:
  ```bash
  python query.py --query "SELECT * FROM table_name LIMIT 5;"
  ```

## CI/CD Integration
This project automates the following tasks with each repository update:
- Data ingestion into the Databricks FileStore.
- Data transformation and loading into the database.
- Query execution and result logging.
