from utils.db import run_query
import streamlit as st

def render():
    # Run the query and get the dataframe
    df = run_query("query_1_4.sql")

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

    st.markdown("""
        - From the query, we can infer that the Click-Through Rate (CTR) is high, indicating that a significant percentage of users who viewed the product pages clicked on them. This suggests effective product page design and user engagement.
        - A high CTR is generally a positive sign, as it indicates that users find the product pages appealing and relevant to their interests. This can lead to higher conversion rates and sales.
        - Expected CTR values can vary widely depending on the industry, product type, and marketing strategies. However, a CTR above 2% is often considered good in e-commerce contexts.
                """)

render()