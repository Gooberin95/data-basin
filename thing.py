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

# Connect to Azure SQL
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Test connection
    cursor.execute("SELECT 1")
    result = cursor.fetchone()

    if result:
        print("✅ Connection to the database was successful!")

        # Generate the SQL INSERT statement dynamically
        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"

        # Insert data row by row
        for _, row in df.iterrows():
            cursor.execute(insert_query, tuple(row[column] for column in column_names))

        # Commit changes
        conn.commit()
        print("✅ Data successfully inserted into the table!")

    # Close connection
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print("❌ Error:", e)

