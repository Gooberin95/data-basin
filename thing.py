import os
from dotenv import load_dotenv
import pyodbc
import pandas as pd

# Load environment variables
load_dotenv()

# File path (Ensure the path is correctly formatted)
csv_file_path = r"C:\Users\Sober\Downloads\house-price.csv"

# Read CSV file
df = pd.read_csv(csv_file_path)

# Get connection details from .env
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Create connection string
conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Define the table name
table_name = "Homes"

# Define column names in a list (Easier to modify later)
column_names = [
    "price", "area", "bedrooms", "bathrooms", "stories", "mainroad",
    "guestroom", "basement", "hotwaterheating", "airconditioning",
    "parking", "prefarea", "furnishingstatus"
]

# Convert column list to a string for SQL query
columns_str = ", ".join(column_names)
placeholders = ", ".join(["?"] * len(column_names))  # Generate ?, ?, ?, ... dynamically


try:
    #Connect to Azure sql
    conn = pyodbc.connect(conn_str)
    # Set what query we will run
    query = f"SELECT * FROM  {table_name}"
    #Read data into a Panda DataFrame
    df = pd.read_sql(query, conn)

    conn.close()

    df.to_excel("output.xlsx", index=False)
    



except pyodbc.Error as e:
    print("❌ Error:", e)

