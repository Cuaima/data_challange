from sklearn.linear_model import LinearRegression
import numpy as np

def stochastic_regression_impute(df, target_col, feature_cols):
    # 1. Split data
    known = df[df[target_col].notnull()]
    unknown = df[df[target_col].isnull()]

    if unknown.empty:
        return df  # Nothing to impute

    # 2. Fit regression model
    model = LinearRegression()
    model.fit(known[feature_cols], known[target_col])

    # 3. Predict for missing
    predictions = model.predict(unknown[feature_cols])

    # 4. Calculate residual std
    residuals = known[target_col] - model.predict(known[feature_cols])
    std_dev = residuals.std()

    # 5. Add stochastic noise
    noise = np.random.normal(0, std_dev, size=len(predictions))
    imputed_values = predictions + noise

    # 6. Update the DataFrame
    df.loc[df[target_col].isnull(), target_col] = imputed_values

    return df
