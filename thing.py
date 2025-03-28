import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
# Load environment variables
load_dotenv()
# C:\Users\Sober\Downloads

#csv_file_path = r"C:\\Users\\Sober\\Downloads\\freelancer_earnings_bd.csv"

#df = pd.read_csv(csv_file_path)



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
       
    #    Index(['Freelancer_ID', 'Job_Category', 'Platform', 'Experience_Level',
    #    'Client_Region', 'Payment_Method', 'Job_Completed', 'Earnings_USD',
    #    'Hourly_Rate', 'Job_Success_Rate', 'Client_Rating', 'Job_Duration_Days',
    #    'Project_Type', 'Rehire_Rate', 'Marketing_Spend'],
    #   dtype='object')
    
        query = " SELECT * FROM Homes WHERE Hourly_Rate > 50";
        df = pd.read_sql(query, engine)

        print(df)
        
       # df.to_sql("Homes", con=engine, if_exists="replace", index=False)
        #print("Data has now been inserted")

        df.to_excel("Data_entry_50$.xlsx", index=False)
    #    print("The data has now been saved to an Excel file")


except Exception as e:
    print(f"❌ Connection failed: {e}")
