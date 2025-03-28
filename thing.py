import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
# Load environment variables
load_dotenv()
# C:\Users\Sober\Downloads

csv_file_path = r"C:\\Users\\Sober\\Downloads\\student_depression_dataset.csv"

df = pd.read_csv(csv_file_path)



# Get credentials

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Create connection string
engine = create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server")

# Test connection
try:
    with engine.connect() as conn:
        print("✅ Connection successful!")

except Exception as e:
    print(f"❌ Connection failed: {e}")


 

def select_all():
    try:
        query = "SELECT * FROM HOMES"
        df = pd.read_sql(query, engine)
        print(df)
    except Exception as e:
        print("Function failed because {e}")
        


def insert_into_excel():
    try:

        query = "SELECT * FROM Homes"
        df = pd.read_sql(query, engine)
        df.to_excel("Two_College_Info.xlsx", index=False)
        print("The data has now been saved to an Excel file")
    except Exception as e:
        print(f"function failed because of {e}")


def replace_table_data():
    try:

        df.to_sql("Homes", con=engine, if_exists="replace", index=False)
        print("Data has now been inserted")
    except Exception as e:
        print("Function failed because of {e}")


select_all()
