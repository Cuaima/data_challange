from utils.db import run_query
import streamlit as st

def render():
    # Run the query and get the dataframe
    df = run_query("query_1_4.sql")
    
    st.subheader("Click-Through Rate (CTR) by Device")

    # Extract the CTR value from the dataframe
    if not df.empty and 'ctr_percentage' in df.columns:
        ctr_value = df['ctr_percentage'].iloc[0]
    else:
        ctr_value = 0.0  # fallback value if data is missing
    
    # Display a centered metric with styling using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div style="text-align:center; padding:20px; background-color:#f0f2f6; border-radius:12px;">
            <h4>Click-Through Rate (CTR)</h4>
            <h1 style="color:#1f77b4;">{ctr_value:.2f}%</h1>
        </div>
        """, unsafe_allow_html=True)

render()