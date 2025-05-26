import streamlit as st
from scripts.kfold import evaluate_with_kfold
from scripts.section3.section3_processing import process_features



def render():
    features = process_features()

    with st.container():
        st.title("Section 3: Model Evaluation and Feature Importance")
        st.markdown("""
            In this section, we will evaluate the model using K-Fold Cross-Validation and analyze feature importance.
            The goal is to understand how well our model performs and which features contribute most to the predictions.
        """)
    # Define target and predictors
    target = 'total_amount'
    X = features.drop(columns=[target])
    y = features[target]

    # Evaluate using K-Fold Cross-Validation
    st.subheader("Model Evaluation with K-Fold Cross-Validation")
    evaluate_with_kfold(X, y, k=5)


render()