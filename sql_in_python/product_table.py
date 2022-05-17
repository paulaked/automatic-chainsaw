import pyodbc
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

class NWProducts:

    def __init__(self):
        self.server = '18.170.54.198'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.northwind_con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE='
                                       + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.engine = sqlalchemy.create_engine(f"mssql+pyodbc://{self.username}:{self.password}@{self.server}/{self.database}?driver={'ODBC+Driver+17+for+SQL+Server'}")
        self.sqlalchemy_con = self.engine.connect()
        self.cursor = self.northwind_con.cursor()
        self._table_list = []


    def _sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def return_all_products(self):
        query_records = self._sql_query("SELECT * FROM Products")
        return query_records.fetchall()

    def return_avg_unit_price(self):
        query_records = self._sql_query("SELECT AVG(UnitPrice) FROM Products")
        return query_records.fetchall()

    def get_list_of_tables(self):
        tables = self.cursor.tables()
        for table in tables:
            if table[1] == 'dbo' and table[3] == 'TABLE':
                self._table_list.append(table[2])
        return self._table_list

    def turn_table_to_df(self, table_name):
        df = pd.read_sql_table(table_name=table_name,con=self.sqlalchemy_con)
        return df

    def df_to_sql(self, table_name, message):
        df = self.turn_table_to_df(table_name)
        df['new'] = message
        df.to_sql('paula',con=self.engine, if_exists='replace')

    def check_new_table(self):
        return self.engine.execute("SELECT * FROM paula").fetchall()