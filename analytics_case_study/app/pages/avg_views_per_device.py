from utils.db import run_query
import streamlit as st
import altair as alt

def render():
    df3 = run_query("query_1_3.sql")

    st.subheader("Average Page Views per Device")
    # st.dataframe(df3)

    # Create a bar chart
    chart = alt.Chart(df3).mark_bar().encode(
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

render()