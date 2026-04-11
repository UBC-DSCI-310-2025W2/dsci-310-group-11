import pandas as pd

EXPECTED_COLUMNS = [
    "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
    "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density",
    "pH", "sulphates", "alcohol", "quality"
]


def validate_raw_data(df):
    # 1. Correct column names
    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # 2. Correct data types
    for col in EXPECTED_COLUMNS:
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise TypeError(f"'{col}' must be numeric")

    # 3. No empty rows
    if df.isnull().all(axis=1).any():
        raise ValueError("Dataset contains completely empty rows")

    # 4. Missingness below 5% per column
    for col in df.columns:
        if df[col].isnull().mean() > 0.05:
            raise ValueError(f"'{col}' exceeds 5% missing values")

    # 5. No duplicate rows
    if df.duplicated().any():
        raise ValueError(f"Dataset contains {df.duplicated().sum()} duplicate rows")

    # 6. No negative values in numeric columns
    if (df[EXPECTED_COLUMNS] < 0).any().any():
        raise ValueError("Dataset contains unexpected negative values")

    # 7. Quality scores in valid range
    if not df["quality"].between(0, 10).all():
        raise ValueError("Quality scores outside expected range [0, 10]")

    # 8. Quality has more than one unique value
    if df["quality"].nunique() < 2:
        raise ValueError("Quality column has only one unique value")

    print("All raw data validation checks passed.")


def validate_processed_data(df):
    # 9. Label column has only expected categories
    unexpected = set(df["label"].unique()) - {"Good", "Bad"}
    if unexpected:
        raise ValueError(f"Unexpected label categories: {unexpected}")
    print("All processed data validation checks passed.")


def validate_split(X_train, X_test):
    # No data leakage between train and test
    overlap = set(X_train.index) & set(X_test.index)
    if overlap:
        raise ValueError(f"Data leakage: {len(overlap)} rows in both train and test")
    print("Train/test split validation passed.")
