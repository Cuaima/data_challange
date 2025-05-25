import os
import sqlite3
import pandas as pd

# Path to the SQLite database and queries
conn = os.path.abspath("../data_challange/analytics_case_study/data/website_data.db")
queries_path = os.path.abspath("../data_challange/analytics_case_study/queries/")

# Establish a connection to the SQLite database
def get_connection(path=conn):
    return sqlite3.connect(path)

# def load_query(query):
#     """read sql query."""
#     with open(queries_path + query, 'r') as file:
#         return file.read()
    
# def run_query(query, path=conn):
#     return pd.read_sql_query(load_query(query), path)
    
def load_query(query_file):
    full_path = os.path.join(queries_path, query_file)
    with open(full_path, 'r') as file:
        return file.read()

def run_query(query_file):
    query = load_query(query_file)
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df