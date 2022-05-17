import pyodbc

server = '18.170.54.198'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

northwind_con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='
                               +database+';UID='+username+';PWD='+password)

cursor = northwind_con.cursor()

customers = cursor.execute("SELECT * FROM Customers")

# for customer in customers:
#     print(customer.CustomerID)

#print(customers.fetchall())


customers_in_paris = cursor.execute("SELECT * FROM Customers WHERE city = 'Paris'").fetchall()

#print(customers_in_paris)

#print(cursor.execute("SELECT * FROM Products").fetchall())

