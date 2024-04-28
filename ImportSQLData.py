import pyodbc
import pandas as pd

conn_str = 'DRIVER={ODBC Driver 11 for SQL Server};SERVER=.\SQLEXPRESS;DATABASE=AdventureWorks2019;Trusted_Connection=yes'

conn = pyodbc.connect(conn_str)

sql = 'SELECT TOP 10 * FROM [Person].[BusinessEntity]'

df = pd.read_sql_query(sql,conn)
print(df.head())


