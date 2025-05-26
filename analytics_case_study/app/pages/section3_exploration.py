import streamlit as st
from scripts.kfold import evaluate_with_kfold
from pages.section3_processing import process_features



def render():
    features = process_features()

    # Define target and predictors
    target = 'total_amount'
    X = features.drop(columns=[target])
    y = features[target]

    # Evaluate using K-Fold Cross-Validation
    st.subheader("Model Evaluation with K-Fold Cross-Validation")
    evaluate_with_kfold(X, y, k=5)


render()