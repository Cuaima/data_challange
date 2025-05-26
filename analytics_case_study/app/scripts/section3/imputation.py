from scripts.stochastic_regression import stochastic_regression_impute
import pandas as pd

def impute_numerical(features, target='price_per_unit', predictors=['quantity', 'conversion_lag']):
    """
    Impute missing numerical values using stochastic regression imputation.
    Args:
        features (DataFrame): DataFrame containing the features.
        target (str): The target column to impute.
        predictors (list): List of predictor columns to use for imputation.
    Returns:
        DataFrame: DataFrame with imputed values.
    """
    valid_rows = features[predictors + [target]].dropna()
    if len(valid_rows) >= 10:
        return stochastic_regression_impute(features, target_col=target, feature_cols=predictors)
    return features

def impute_categorical(features, categorical_cols):
    for col in categorical_cols:
        if features[col].isnull().any():
            features[col] = features[col].fillna(features[col].mode()[0])
    return features
