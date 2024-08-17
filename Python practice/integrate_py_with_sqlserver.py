# step 1. To integrate we need either pyodbcc or pymssql
# step 2. sertting up database in ms sql 
# step 3. Using pyodbc create a python srript to connect to ms sql
import pyodbc

try:
    database_name = input("Enter a databse name to create")
    c = pyodbc.connect
    (
        'DRIVER = {SQL Server};'
        'server = LAPTOP-BK822L27\SQLEXPRESS;'
        'database = pydb;'
        'Trusted_Connection=True;'
    )
    
    c.autocommit = True
    c.execute(f'Drop database {database_name}')
    c.execute(f'Create database {database_name}')
    print("database created")
    print("connected to Sql server")  
except pyodbc.error as ex:
    print("connection failed",ex)