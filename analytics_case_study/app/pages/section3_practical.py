import streamlit as st
import pandas as pd
from datetime import datetime
from utils.db import get_connection
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PowerTransformer, StandardScaler
from scripts.stochastic_regression import stochastic_regression_impute
from scripts.outliers import remove_outliers_iqr
import plotly.express as px

def render():
    st.subheader("Practical Section: Feature Engineering and Data Preparation")

    ##### Data Retrieval and Preparation #####
    ### Retrieval of data from SQLite database
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

    def prepare_features():
        # Load all tables
        users, orders, order_items, products, page_views = load_data()

        # Convert date columns to datetime
        users['registration_date'] = pd.to_datetime(users['registration_date'])
        orders['order_date'] = pd.to_datetime(orders['order_date'])

        # Merge data
        df = orders.merge(users, on="user_id", how="left")
        df = df.merge(order_items, on="order_id", how="left")
        df = df.merge(products, on="product_id", how="left")

        # Derived feature: conversion lag
        df['conversion_lag'] = (df['order_date'] - df['registration_date']).dt.days

            # Find the most common device_type per user from page_views (using mode)
        device_type_per_user = (
            page_views.groupby('user_id')['device_type']
            .agg(lambda x: x.mode().iat[0] if not x.mode().empty else None)
            .reset_index()
        )

        # Join device_type into main dataframe on user_id
        df = df.merge(device_type_per_user, on='user_id', how='left')
        
        # Select features
        features = df[[
            'total_amount',
            'country',
            'user_segment',
            'quantity',
            'price_per_unit',
            'category',  # product category
            'conversion_lag',
            'device_type',  # most common device type per user
        ]]

        return features
    
    def process_features():
        """Prepare and encode features for modeling."""
        features = prepare_features()

        # Handle missing numerical values with stochastic regression imputation
        numerical_target = 'price_per_unit'
        numerical_features = ['quantity', 'conversion_lag']

        # Only apply if all numerical predictors are non-null
        valid_rows = features[numerical_features + [numerical_target]].dropna()
        if len(valid_rows) >= 10:  # arbitrary minimum sample size
            features = stochastic_regression_impute(
                df=features,
                target_col=numerical_target,
                feature_cols=numerical_features
            )

        # Define categorical columns
        categorical_cols = ['country', 'user_segment', 'category', 'device_type']

        # Ensure columns exist in the DataFrame
        existing_cols = [col for col in categorical_cols if col in features.columns]

        # Impute missing values with mode (most frequent value)
        for col in existing_cols:
            if features[col].isnull().any():
                mode_value = features[col].mode(dropna=True)
                if not mode_value.empty:
                    features[col] = features[col].fillna(mode_value[0])

        # Apply one-hot encoding (drop_first=True to reduce multicollinearity)
        features_encoded = pd.get_dummies(features, columns=existing_cols, drop_first=True)

        # Define numerical columns
        numerical_cols = ['quantity', 'price_per_unit', 'conversion_lag']

        if not features_encoded[numerical_cols].empty:
            for feature in features_encoded:
                features_encoded[feature] = remove_outliers_iqr(features_encoded, feature)

        # Scale numerical features
        scaler = StandardScaler()
        if not features_encoded[numerical_cols].empty:
            features_encoded[numerical_cols] = scaler.fit_transform(features_encoded[numerical_cols])

        return features_encoded
    


    # Account for skewing
    def handle_skewness(df, target_col):
        """Apply Power Transformation to reduce skewness."""
        pt = PowerTransformer(method='yeo-johnson', standardize=True)
        df[target_col] = pt.fit_transform(df[[target_col]])
        return df
    
    features = process_features()

    features = handle_skewness(features, 'total_amount')


    st.dataframe(features.head())

    ###########################################################

    st.subheader("Total Order Amount")

    fig = px.histogram(
        features,
        x='total_amount',
        nbins=30,
        title="Distribution of Total Order Amount",
        labels={'total_amount': 'Total Order Amount (€)'},
        color_discrete_sequence=['skyblue']
    )


    fig.update_traces(opacity=0.6)
    st.plotly_chart(fig, use_container_width=True)

    ######################
    # Show preview of dataframe
    st.subheader("Feature Data Preview")
    st.dataframe(features.head())

    # Show distribution of target
    st.subheader("Total Order Amount Distribution")

    fig, ax = plt.subplots()
    ax.hist(features['total_amount'], bins=20, color='skyblue', edgecolor='black')
    ax.set_xlabel('Total Order Amount')
    ax.set_ylabel('Number of Orders')
    st.pyplot(fig)

    # Show correlation heatmap
    st.subheader("Feature Correlation")
    # st.write(features.corr(numeric_only=True))
    fig, ax = plt.subplots()
    sns.heatmap(features.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

render()