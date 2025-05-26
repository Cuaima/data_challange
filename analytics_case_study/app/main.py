import streamlit as st
from pages import section1, section2 , section3, section3_exploration

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

# Configure the main content area
with st.container():
    configure_overview()

# Render the sections of the dashboard 
section1.render()

section2.render()

section3.render()

section3_exploration.render()
