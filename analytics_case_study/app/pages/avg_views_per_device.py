from utils.db import run_query
import streamlit as st
import altair as alt

def render():
    df = run_query("query_1_3.sql")

    # Create a bar chart
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("device_type:N", title="Device Type", axis=alt.Axis(labelAngle=0)),
        y=alt.Y("avg_page_views_per_session:Q", title="Avg. Page Views per Session"),
        color=alt.Color("device_type:N", legend=None),
        tooltip=["device_type", "avg_page_views_per_session"]
    ).properties(
        width=600,
        height=400,
        title="Avg. Page Views per Session by Device"
    )

    st.altair_chart(chart, use_container_width=True)

    st.markdown("""
        - This chart shows that we are getting more page views from desktop devices compared to mobile and tablet devices.
        - This could indicate that users prefer browsing the platform on larger screens, which may provide a better user experience.
        - To improve mobile engagement, consider optimizing the mobile user interface and ensuring that the mobile experience is as seamless as possible.
        - Additionally, analyzing user behavior on different devices can help identify specific areas for improvement in the mobile experience.
    """)

render()