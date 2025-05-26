from utils.db import run_query
import streamlit as st
import altair as alt
import pandas as pd

def render():
    # Run the SQL query
    df = run_query("query_1_1.sql")


    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('total_quantity:Q', title='Total Units Sold'),
        y=alt.Y('product_name:N', sort='-x', title='Product Name'),
        tooltip=['product_name', 'total_quantity']
    ).properties(
        height=400,
        width='container',
        title="Top 10 Products by Quantity Sold"
    )

    st.altair_chart(chart, use_container_width=True)



render()