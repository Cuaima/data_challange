from utils.db import run_query
import streamlit as st

def render():
    # Query for users registered in the last 6 months but never ordered
    df_never_ordered = run_query("query_1_2.sql")

    st.subheader("Users Registered in the Last 6 Months but Never Placed an Order")

    # KPI: number of users found
    col1, col2 = st.columns([2,2])
    with col1:
        st.markdown("""
        <div style="text-align:center; padding:20px; background-color:#f0f2f6; border-radius:12px;">
            <h4> Users Without Orders:</h4>
            <h1 style="color:#1f77b4;">{:,}</h1>
        </div>
    """.format(len(df_never_ordered)), unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Downloadable CSV
        st.download_button(
            label="Download User List as CSV",
            data=df_never_ordered.to_csv(index=False),
            file_name="never_ordered_users.csv",
            mime="text/csv"
        )
    
    with col2:
        # Data preview
        st.subheader("User List:")
        st.dataframe(df_never_ordered)
