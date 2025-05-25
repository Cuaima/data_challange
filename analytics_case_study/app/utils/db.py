import os
import sqlite3
import pandas as pd
import streamlit as st

# Path to the SQLite database and queries
conn = os.path.abspath("../data_challange/analytics_case_study/data/website_data.db")
queries_path = os.path.abspath("../data_challange/analytics_case_study/queries/")

# Establish a connection to the SQLite database
def get_connection(path=conn):
    return sqlite3.connect(path)

# Part 1 functions for loading and running SQL queries:
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

# Part 2 functions for loading and running SQL queries:
# def load_data():
#     """Load data from the SQLite database."""
#     conn = get_connection()

#     ad_impressions = pd.read_sql("SELECT * FROM ad_impressions", conn)
#     ad_clicks = pd.read_sql("SELECT * FROM ad_clicks", conn)
#     page_views = pd.read_sql("SELECT * FROM page_views", conn)
#     orders = pd.read_sql("SELECT * FROM orders", conn)

#     conn.close()

#     # Return the dataframes as a dictionary
#     return {
#         "ad_impressions": ad_impressions,
#         "ad_clicks": ad_clicks,
#         "page_views": page_views,
#         "orders": orders
#     }