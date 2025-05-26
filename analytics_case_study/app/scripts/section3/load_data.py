import pandas as pd
from utils.db import get_connection
import streamlit as st

@st.cache_data
def load_data():
    """Load data from the SQLite database.
    Returns:
        tuple: DataFrames for users, orders, order_items, products, and page_views.
    """
    
    conn = get_connection()
    users = pd.read_sql("SELECT user_id, registration_date, country, user_segment FROM users", conn)
    orders = pd.read_sql("SELECT order_id, user_id, order_date, total_amount FROM orders", conn)
    order_items = pd.read_sql("SELECT order_id, product_id, quantity, price_per_unit FROM order_items", conn)
    products = pd.read_sql("SELECT product_id, category FROM products", conn)
    page_views = pd.read_sql("SELECT user_id, session_id, device_type FROM page_views", conn)
    conn.close()
    return users, orders, order_items, products, page_views