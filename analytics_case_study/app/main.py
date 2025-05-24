import streamlit as st
import sqlite3
import pandas as pd
import altair as alt

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

# Establish a connection to the SQLite database
conn = sqlite3.connect("/Users/claudiagroot/Documents/Code/data_challange/analytics_case_study/data/website_data.db")
queries_path = "/Users/claudiagroot/Documents/Code/data_challange/analytics_case_study/queries/"

def load_query(query):
    """read sql query."""
    with open(query, 'r') as file:
        return file.read()

# Load Queries
top_products = load_query(queries_path + "query_1_1.sql")
never_ordered = load_query(queries_path + "query_1_2.sql")
avg_page_views_per_device = load_query(queries_path + "query_1_3.sql")
ctr = load_query(queries_path + "query_1_4.sql")
# mom_growth_rate = load_query(queries_path + "query_1_5.sql")
# avg_days_to_first_order = load_query(queries_path + "query_1_6.sql")
# most_viewed_category = load_query(queries_path + "query_1_7.sql")

# Run query and get dataframes
df_top_products = pd.read_sql_query(top_products, conn)
df_never_ordered = pd.read_sql_query(never_ordered, conn)
df_avg_page_views_per_device = pd.read_sql_query(avg_page_views_per_device, conn)
df_ctr = pd.read_sql_query(ctr, conn)
# df_mom_growth_rate = pd.read_sql_query(mom_growth_rate, conn)
# df_avg_days_to_first_order = pd.read_sql_query(avg_days_to_first_order, conn)
# df_most_viewed_category = pd.read_sql_query(most_viewed_category, conn)

st.subheader("Top 10 Most Frequently Purchased Products")
st.dataframe(df_top_products)

st.subheader("Users Registered in the Last 6 Months but Never Placed an Order")
st.dataframe(df_never_ordered)

st.subheader("Average Page Views per Device")
st.dataframe(df_avg_page_views_per_device)

st.subheader("Click-Through Rate (CTR) by Device")
st.dataframe(df_ctr)

# st.subheader("Month-over-Month Growth Rate")
# st.dataframe(df_mom_growth_rate)

# st.subheader("Average Days to First Order")
# st.dataframe(df_avg_days_to_first_order)

# st.subheader("Most Viewed Category")
# st.dataframe(df_most_viewed_category)
