import streamlit as st

def render():
    with st.container():
        st.header("Section 2: Data Analysis & Interpretation")
    
    with st.expander("Customer Journey Analysis"):
        st.markdown("""
            ### Describe how you would approach an analysis to understand the customer journey from the first ad impression to a purchase. 
            ### Which tables are key, and what steps would you take?
                    """)
        
        st.markdown("""
                
            To analyze the customer journey from the first ad impression to a purchase, I would follow these steps:
            
            ### 1. **Identify Key Tables**: 
                - **`ad_impressions`**: Logs when a user saw an ad.
                - **`ad_clicks`**: Logs when a user clicked on an ad.
                - **`page_views`**: Shows what users do on the website after the click.
                - **`orders`**: Contains purchase details, including timestamps and user IDs.
                - **`users`**: Adds context such as registration date, country, and segment.
                
            ### 2. **Data Preparation**:
            - Load the data from the SQLite database using SQL queries.
            - Clean and preprocess: handle missing values, convert timestamps, anonymize personal information, and remove test data if any.
            
            ### 3. **Join Tables**:
            - Join the `ad_impressions`, `ad_clicks`, `page_views`, and `orders` tables on user IDs and timestamps to create a unified view of the customer journey.
                - Extract users from `ad_impressions` and note the earliest impression timestamp.
                - Join with `ad_clicks` on `impression_id` and `user_id` to find when users clicked on ads.
                - Join with `page_views` using `user_id` and compare `timestamp` to track user activity on the site.
                - Join with `orders` on `user_id` and filter orders placed after the initial click or impression.
                - Potentially join with the `users` table to add user metadata like registration date, country, and segment.
            This sequence ensures we capture the entire journey from ad impression, to click, to page views, and finally to purchase.
            
            ### 4. **Analysis**:
            - Calculate the time taken from the first ad impression to the first click, and from the first click to the first purchase.
            - Analyze the conversion rates at each step of the journey (impression to click, click to purchase).
            - Segment the analysis by user demographics (e.g., country, segment) to identify patterns.
            - Visualize the data using charts to show the flow of users through the journey, highlighting drop-off points.
            
            ### 5. **Insights**:
            - Identify which ads or channels lead to the highest conversion rates.
            - Determine the average /median conversion time.
            - Highlight any significant drop-off points in the customer journey.
            - Provide recommendations for optimizing ad strategies based on user behavior and conversion patterns.           
        """)

    with st.expander("Using Segments to Drive Business Decisions"):
        st.markdown("""
            ### How would you use the segments in the `users` table to drive business decisions? 
            ### Provide examples of how different segments might lead to different marketing strategies.
        """)
        
        st.markdown("""
            Segmentation is crucial for targeted marketing and personalized user experiences. 
            Here’s how I would use the segments in the `users` table to drive business decisions:
            
            ### 1. **Tailor Marketing Strategies**:
                - Use tailored advertising, emails, and offers based on user segments.
                - For example, target `casual` users with introductory offers to encourage purchases, while `engaged` users might receive loyalty rewards or exclusive deals.
            
            ### 2. **Personalized User Experience**:
                - Reccommend products based on user segments.
                - For instance `researcher` users might receive detailed product comparisons and reviews.
                - Streamlined navigation for `casual` users to quickly find popular products.
                - Advanced features for `engaged` users, such as personalized dashboards or advanced search filters.
                    
            ### 3. **Analyze Segment Performance**:
                - Track the performance of different segments over time to identify trends and adjust strategies accordingly.
                - For instance, if a particular segment shows declining engagement, I would investigate potential causes (e.g., product relevance, pricing) and adapt marketing strategies to re-engage them.
                - Focus on high-value segments, such as `engaged`, ro maximize their lifetime value through targeted retention strategies.
                
            ### 4. **A/B Testing**:
                - Implement A/B testing for different segments to determine which marketing strategies yield the best results.
                - For example, testing different email campaigns for casual users versus engaged users can help refine messaging and improve conversion rates.
                    
            ### 5. **Feedback Loop**:
                - Continuously gather feedback from different segments to understand their needs and preferences better.
                - Use this feedback to iterate on marketing strategies and product offerings, ensuring they remain relevant and effective for each segment.
        """)

render()