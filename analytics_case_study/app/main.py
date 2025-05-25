import os
import streamlit as st
import sqlite3
import pandas as pd
import altair as alt
from utils.db import run_query
from pages import top_products

# Set the page configuration
st.set_page_config(
    page_title="Website Analytics Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

# Set the title of the app
def configure_overview():
    """Configure the overview section of the dashboard."""
    st.title("Website Analytics Dashboard")
    st.markdown("""
        This dashboard provides insights into website analytics, including user behavior, product performance, and sales trends.
        Use the navigation on the left to explore different sections.
    """)

# Configure the sidebar navigation
with st.sidebar:
    st.header("Navigation")
    st.selectbox("Select a section:", ["Overview", "Product Performance", "User Behavior", "Sales Trends"])


# Configure the main content area
with st.container():
    configure_overview()

with st.expander("Queries Overview"):
    left, right = st.columns(2)
    left.subheader("Top 10 Most Frequently Purchased Products")
    right.subheader("Users Registered in the Last 6 Months but Never Placed an Order")



# Run query and get dataframes

df_never_ordered = run_query("query_1_2.sql")
df_avg_page_views_per_device = run_query("query_1_3.sql")
df_ctr = run_query("query_1_4.sql")
df_mom_growth_rate = run_query("query_1_5.sql")
df_avg_days_to_first_order = run_query("query_1_6.sql")
# df_most_viewed_category = run_query("query_1_7.sql")


top_products.render() 

st.subheader("Users Registered in the Last 6 Months but Never Placed an Order")
st.dataframe(df_never_ordered)

st.subheader("Average Page Views per Device")
st.dataframe(df_avg_page_views_per_device)

st.subheader("Click-Through Rate (CTR) by Device")
st.dataframe(df_ctr)

st.subheader("Month-over-Month Growth Rate")
st.dataframe(df_mom_growth_rate)

st.subheader("Average Days to First Order")
st.dataframe(df_avg_days_to_first_order)

# st.subheader("Most Viewed Category")
# st.dataframe(df_most_viewed_category)
