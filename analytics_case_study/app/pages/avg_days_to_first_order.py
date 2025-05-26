from utils.db import run_query
import streamlit as st

def render():
    df = run_query("query_1_6.sql")
    days = df['avg_days_to_first_order'].iloc[0] if not df.empty else 0
    avg_days = f"{days:.2f} days" if days else "No data available"

    st.metric(label="Average Days to First Order", value = avg_days)

    st.markdown("""
        - In this example, the average days to first order seems to be fast (within 3-7 days), indicating that users are quickly engaging with the platform and making purchases after registration.)
                """)

render()

    