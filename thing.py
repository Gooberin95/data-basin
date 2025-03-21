import pyodbc

# Azure SQL Managed Instance Connection Details
server = 'your-server-name.public.{}.database.windows.net'.format('your-region')
database = 'Unicorn'  # Your database name
username = 'your-username'
password = 'your-password'

# Connection string
conn_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

try:
    # Establish Connection
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    
    # Sample Query
    cursor.execute("SELECT TOP 10 * FROM your_table_name")  # Replace with your table name
    
    # Fetch & Print Results
    for row in cursor.fetchall():
        print(row)
    
    # Close Connection
    cursor.close()
    conn.close()

except Exception as e:
    print("Error:", e)
