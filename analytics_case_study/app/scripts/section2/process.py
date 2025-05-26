# Part 2 functions for loading and running SQL queries:
# def load_data():
#     """Load data from the SQLite database."""
#     conn = get_connection()

#     ad_impressions = pd.read_sql("SELECT * FROM ad_impressions", conn)
#     ad_clicks = pd.read_sql("SELECT * FROM ad_clicks", conn)
#     page_views = pd.read_sql("SELECT * FROM page_views", conn)
#     orders = pd.read_sql("SELECT * FROM orders", conn)

#     conn.close()

#     # Return the dataframes as a dictionary
#     return {
#         "ad_impressions": ad_impressions,
#         "ad_clicks": ad_clicks,
#         "page_views": page_views,
#         "orders": orders
#     }