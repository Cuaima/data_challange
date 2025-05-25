import streamlit as st

def render():
    with st.container():
        st.header("Section 2: Data Analysis & Interpretation")
        st.write("""
            - Describe how you would approach an analysis to understand the customer journey from the first ad impression to a purchase. 
            Which tables are key, and what steps would you take?
        """)
        st.write("""
            The purpose of this analysis is to understand how the customer moves from seeing an ad to making a purchase.
            This helps identify bottlenecks, optimize the ad strategy, and improve conversion rates.
                
            To analyze the customer journey from the first ad impression to a purchase, I would follow these steps:
            1. **Identify Key Tables**: 
                - `ad_impressions`: Logs when a user saw an ad.
                - `ad_clicks`: Logs when a user clicked on an ad.
                - `page_views`: Shows what users do on the website after the click.
                - `orders`: Contains purchase details, including timestamps and user IDs.
                - `users`: Adds context with user metadata such as registration date, country, and segment.
                
            2. **Data Preparation**:
            - Load the data from the SQLite database using SQL queries.
            - Clean and preprocess the data to ensure consistency, handle missing values, anonymize private information and convert timestamps to datetime objects.
            3. **Join Tables**:
            - Join the `ad_impressions`, `ad_clicks`, `page_views`, and `orders` tables on user IDs and timestamps to create a unified view of the customer journey.
                - Extract users from `ad_impressions` and note the earliest impression timestamp.
                - Join with `ad_clicks` on `impression_id` and `user_id` to find when users clicked on ads.
                - Join with `page_views` using `user_id` and compare `timestamp` to track user activity on the site.
                - Join with `orders` on `user_id` and filter orders placed after the initial click or impression.
                 
        """)

render()