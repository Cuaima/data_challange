from scripts.outliers import remove_outliers_iqr

def remove_outliers(features, cols):
    for col in cols:
        features = remove_outliers_iqr(features, col)
    return features
