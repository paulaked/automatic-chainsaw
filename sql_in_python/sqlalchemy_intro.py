import sqlalchemy
import pyodbc

server = 'localhost,1433'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = '{ODBC Driver 17 for SQL Server}'

# Connecting with pyodbc
docker_Northwind = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}")
cursor = docker_Northwind.cursor()

# connecting with sqlalchemy
# we need to change the connection string for the driver
# you might need to use 'SQL+Server' instead
driver = 'ODBC+Driver+17+for+SQL+Server'
engine = sqlalchemy.create_engine(f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}")

# open a connection using sqlalchemy
connection = engine.connect()

# once we have a connection open, we can execute multiple different sql queries -
# whether that is just selecting data or actually creating databases and tables

# execute queries
results = engine.execute('SELECT * FROM Products;') # this will return an object we will need to access
print(results)

# retrieve one row at a time from your result
first_row = results.fetchone()
print(first_row)

# retrieve multiple rows at a time
many_rows = results.fetchmany(10) # here we will need to specify how many we want to retrieve
print(many_rows)

# retrieving everything
all_results = results.fetchall()
print(all_results)