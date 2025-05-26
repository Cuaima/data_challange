from utils.db import run_query
import streamlit as st
import altair as alt

def render():
    df = run_query("query_1_5.sql")
    if df.empty:
        st.error("No data available for Month-over-Month Growth Rate.")
        return
    
    latest_growth = df['mom_growth_rate'].iloc[-1]

    st.metric(label="Latest Month-over-Month Growth Rate", value=f"{latest_growth:.2f}%")
    st.write("This metric shows the percentage change in the number of unique users from one month to the next.")
   

    # Create a combined 'year-month' field for better x-axis labels
    df['year_month'] = df['year'] + "-" + df['month']

    # Create a line chart for the growth rate
    chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X('year_month', sort=None, title='Month'),
        y=alt.Y('mom_growth_rate', title='MoM Growth Rate (%)'),
        tooltip=['year_month', 'mom_growth_rate']
    ).properties(
        width=700,
        height=400
    )

    st.subheader("Month-over-Month Growth Rate")
    st.altair_chart(chart, use_container_width=True)

    st.markdown("""
        - The Month-over-Month (MoM) Growth Rate indicates how the number of unique users has changed from one month to the next. A positive growth rate suggests an increase in user engagement, while a negative rate indicates a decline.
        - In this case, the latest MOM growth rate is negative, which suggests there might be issues with one of the following:
                - Issues with user experience or product offerings.
                - Increased competition in the market.
                - Marketing strategies that may not be resonating with the target audience.
                - Technical issues that may have affected user access or engagement.
        - To improve the MoM growth rate, consider:
            - Analyzing user feedback to identify pain points.
            - Enhancing marketing strategies to better reach and engage the target audience.
            - Implementing A/B testing to optimize user experience and product offerings.
                """)

render()