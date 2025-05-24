import os
import sys 
import sqlite3
import pandas as pd

sql_path = "/Users/claudiagroot/Documents/Code/data_challange/analytics_case_study/queries/"
db_path = "/Users/claudiagroot/Documents/Code/data_challange/analytics_case_study/data/website_data.db"

# Establish a connection to the database
connection = sqlite3.connect(db_path)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Example SQL query
query = "SELECT name FROM sqlite_master WHERE type='table';"

# Execute the query
cursor.execute(query)

# Fetch all results
tables = cursor.fetchall()

# Query 1.1: Top 10 most frequently purchased products
with open(sql_path + "query_1_1.sql") as file:
    query_1_1 = file.read()

df1 = pd.read_sql_query(query_1_1, connection)
# print(df1)

# Query 1.2: Identifty users who registered in the last 6 months but never placed an order
with open(sql_path + "query_1_2.sql") as file:
    query_1_2 = file.read()

df2 = pd.read_sql_query(query_1_2, connection)
# print(df2)

# Close the connection
connection.close()
