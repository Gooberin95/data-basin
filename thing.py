import os
from dotenv import load_dotenv
import pyodbc

# Load environment variables
load_dotenv()

# Get connection details from .env
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Create connection string
conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Connect to Azure SQL
conn = pyodbc.connect(conn_str)
print("Connected successfully!")
