import streamlit as st
from . import top_products, never_ordered, avg_views_per_device, ctr, mom_growth_rate, avg_days_to_first_order

def render():
    with st.container():
        st.header("Section 1: SQL & Data Retrieval")
        st.write("""
            In this section, we will retrieve data from the database using SQL queries.
            The data will be used to generate various visualizations and insights.
        """)
        st.markdown("""
            **Note:** The SQL queries are not shown here, but they are executed in the background to fetch the required data.
        """)
    #     left, right = st.columns(2)
    #     left.subheader("Top 10 Most Frequently Purchased Products")
    #     right.subheader("Users Registered in the Last 6 Months but Never Placed an Order")

    with st.expander("Top 10 Most Frequently Purchased Products"):
        # st.write("This section displays the top 10 products based on the total quantity sold.")
        top_products.render()

    with st.expander("Users Registered in the Last 6 Months but Never Placed an Order"):
        st.write("This section shows users who registered in the last 6 months but have never placed an order.")
        never_ordered.render()  

    with st.expander("Average Views per Device"):
        st.write("This section displays the average number of views per device type.")
        avg_views_per_device.render()

    with st.expander("Click-Through Rate (CTR)"):
        st.write("This section shows the click-through rate (CTR) for the website.")
        ctr.render()

    with st.expander("Month-over-Month Growth Rate"):
        st.write("This section displays the month-over-month growth rate of the website.")
        mom_growth_rate.render()

    with st.expander("Average Days to First Order"):
        st.write("This section shows the average number of days it takes for a user to place their first order after registration.")
        avg_days_to_first_order.render()

render()