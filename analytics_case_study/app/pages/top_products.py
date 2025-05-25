from utils.db import run_query
import streamlit as st

def render():
    """Render the top products page."""
    st.title("Top Products")
    st.markdown("""
        This page displays the top 10 most frequently purchased products.
        Use the navigation on the left to explore different sections of the dashboard.
    """)
    df_top_products = run_query("query_1_1.sql")

    st.subheader("Top 10 Most Frequently Purchased Products")
    st.dataframe(df_top_products)