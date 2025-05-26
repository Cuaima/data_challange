import streamlit as st
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score



def evaluate_with_kfold(X, y, k=5):
    kf = KFold(n_splits=k, shuffle=True, random_state=42)
    model = LinearRegression()

    mse_scores = []
    r2_scores = []

    fold = 1
    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        mse_scores.append(mse)
        r2_scores.append(r2)

        st.write(f"Fold {fold} - MSE: {mse:.4f}, R²: {r2:.4f}")
        fold += 1

    st.success(f"Average MSE: {np.mean(mse_scores):.4f}")
    st.success(f"Average R²: {np.mean(r2_scores):.4f}")