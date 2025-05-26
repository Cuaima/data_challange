import streamlit as st
import pandas as pd
from utils.db import get_connection
from sklearn.preprocessing import PowerTransformer, StandardScaler
from scripts.stochastic_regression import stochastic_regression_impute
from scripts.outliers import remove_outliers_iqr
import matplotlib.pyplot as plt
import plotly.express as px


st.subheader("Practical Section: Feature Engineering and Data Preparation")

@st.cache_data
def load_data():
    conn = get_connection()

    users = pd.read_sql("""
        SELECT user_id, registration_date, country, user_segment 
        FROM users
    """, conn)

    orders = pd.read_sql("""
        SELECT order_id, user_id, order_date, total_amount 
        FROM orders
    """, conn)

    order_items = pd.read_sql("""
        SELECT order_id, product_id, quantity, price_per_unit 
        FROM order_items
    """, conn)

    products = pd.read_sql("""
        SELECT product_id, category 
        FROM products
    """, conn)

    page_views = pd.read_sql("""
        SELECT user_id, session_id, device_type 
        FROM page_views
    """, conn)

    conn.close()
    return users, orders, order_items, products, page_views

def prepare_features(): # FIXME: this function does too much, consider breaking it down
    users, orders, order_items, products, page_views = load_data()

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
        'total_amount',
        'country',
        'user_segment',
        'quantity',
        'price_per_unit',
        'category',
        'conversion_lag',
        'device_type',
    ]]

def process_features(): # FIXME: this function does too much, consider breaking it down
    features = prepare_features()

    # Handle numerical missing values using stochastic regression imputation
    numerical_target = 'price_per_unit'
    numerical_features = ['quantity', 'conversion_lag']

    valid_rows = features[numerical_features + [numerical_target]].dropna()
    if len(valid_rows) >= 10:
        features = stochastic_regression_impute(
            df=features,
            target_col=numerical_target,
            feature_cols=numerical_features
        )

    # Remove outliers BEFORE encoding and scaling
    for col in ['total_amount', 'price_per_unit', 'quantity']:
        features = remove_outliers_iqr(features, col)

    # Handle skewness
    pt = PowerTransformer(method='yeo-johnson', standardize=False)
    for col in ['total_amount', 'price_per_unit']:
        features[col] = pt.fit_transform(features[[col]])

    # Scale numeric features
    scaler = StandardScaler()
    numerical_cols = ['total_amount', 'quantity', 'price_per_unit', 'conversion_lag']
    features[numerical_cols] = scaler.fit_transform(features[numerical_cols])

    # Impute categorical
    categorical_cols = ['country', 'user_segment', 'category', 'device_type']
    for col in categorical_cols:
        if features[col].isnull().any():
            features[col] = features[col].fillna(features[col].mode()[0])

    # One-hot encoding
    features = pd.get_dummies(features, columns=categorical_cols, drop_first=True)

    # TODO: Not sure if anonymization is needed here, but potentially could be added
    # Anonymization (if needed)
    # features['user_id'] = features['user_id'].apply(lambda x: hash(x))
    # features['order_id'] = features['order_id'].apply(lambda x: hash(x))

    return features

features = process_features()


