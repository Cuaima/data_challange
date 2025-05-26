import pandas as pd

def merge_and_prepare(users, orders, order_items, products, page_views):
    """ Merge and prepare data for analysis.
    Args:
        users (DataFrame): User data.
        orders (DataFrame): Order data.
        order_items (DataFrame): Order items data.
        products (DataFrame): Product data.
        page_views (DataFrame): Page views data.
    Returns:
        DataFrame: Merged and prepared DataFrame with relevant features.
    """

    
    users['registration_date'] = pd.to_datetime(users['registration_date'])
    orders['order_date'] = pd.to_datetime(orders['order_date'])

    df = orders.merge(users, on="user_id", how="left")
    df = df.merge(order_items, on="order_id", how="left")
    df = df.merge(products, on="product_id", how="left")
    df['conversion_lag'] = (df['order_date'] - df['registration_date']).dt.days

    device_type_per_user = (
        page_views.groupby('user_id')['device_type']
        .agg(lambda x: x.mode().iat[0] if not x.mode().empty else None)
        .reset_index()
    )
    df = df.merge(device_type_per_user, on='user_id', how='left')

    return df[[
        'total_amount', 'country', 'user_segment', 'quantity',
        'price_per_unit', 'category', 'conversion_lag', 'device_type'
    ]]
