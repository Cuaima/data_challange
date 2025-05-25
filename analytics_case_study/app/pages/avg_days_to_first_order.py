from utils.db import run_query
import streamlit as st

def render():
    df_avg_days = run_query("query_1_6.sql")
    days = df_avg_days['avg_days_to_first_order'].iloc[0] if not df_avg_days.empty else 0
    avg_days = f"{days:.2f} days" if days else "No data available"

    st.subheader("Average Days to First Order")
    st.metric(label="Average Days to First Order", value = avg_days)

render()

    