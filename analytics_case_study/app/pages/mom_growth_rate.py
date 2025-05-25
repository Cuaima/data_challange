from utils.db import run_query
import streamlit as st
import altair as alt

def render():
    df_mom_growth_rate = run_query("query_1_5.sql")

    st.subheader("Month-over-Month Growth Rate")
    # st.dataframe(df_mom_growth_rate)
    latest_growth = df_mom_growth_rate['mom_growth_rate'].iloc[-1]

    st.metric(label="Latest Month-over-Month Growth Rate", value=f"{latest_growth:.2f}%")
    st.write("This metric shows the percentage change in the number of unique users from one month to the next.")
   

    # Create a combined 'year-month' field for better x-axis labels
    df_mom_growth_rate['year_month'] = df_mom_growth_rate['year'] + "-" + df_mom_growth_rate['month']

    # Create a line chart for the growth rate
    chart = alt.Chart(df_mom_growth_rate).mark_line(point=True).encode(
        x=alt.X('year_month', sort=None, title='Month'),
        y=alt.Y('mom_growth_rate', title='MoM Growth Rate (%)'),
        tooltip=['year_month', 'mom_growth_rate']
    ).properties(
        width=700,
        height=400
    )

    st.subheader("Month-over-Month Growth Rate")
    st.altair_chart(chart, use_container_width=True)