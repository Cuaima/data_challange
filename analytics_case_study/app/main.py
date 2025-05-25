import streamlit as st
import pandas as pd
import altair as alt
from pages import top_products, avg_days_to_first_order,ctr, mom_growth_rate, avg_views_per_device, never_ordered


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

# # Configure the sidebar navigation
# with st.sidebar:
#     st.header("Navigation")
#     st.selectbox("Select a section:", ["Overview", "Product Performance", "User Behavior", "Sales Trends"])


# Configure the main content area
with st.container():
    configure_overview()

# with st.expander("Queries Overview"):
#     left, right = st.columns(2)
#     left.subheader("Top 10 Most Frequently Purchased Products")
#     right.subheader("Users Registered in the Last 6 Months but Never Placed an Order")

with st.expander("Top 10 Most Frequently Purchased Products"):
    st.write("This section displays the top 10 products based on the total quantity sold.")
    top_products.render()
    

never_ordered.render()
avg_views_per_device.render()
ctr.render()
mom_growth_rate.render()
avg_days_to_first_order.render()


# st.subheader("Most Viewed Category")
# st.dataframe(df_most_viewed_category)
