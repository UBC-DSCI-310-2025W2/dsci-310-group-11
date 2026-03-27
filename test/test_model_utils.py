#test/test_model_utils.py

import pytest
import pandas as pd
from sklearn.linear_model import LogisticRegression
from src.model_utils import train_logistic_regression

def test_train_logistic_regression_success():
    """Test if the function successfully returns a fitted model."""
    x_train = pd.DataFrame({'feature1': [1.5, 2.1, 3.0, 4.2], 'feature2': [0.1, 0.2, 0.3, 0.4]})
    y_train = pd.Series(['Good', 'Bad', 'Good', 'Bad'])
    
    model = train_logistic_regression(x_train, y_train)
    assert isinstance(model, LogisticRegression), "Model should be a LogisticRegression instance."
    assert hasattr(model, 'classes_'), "Model should be fitted (have classes_ attribute)."
    
    
    
def test_train_logistic_regression_value_error():
    """Test if the function raises a ValueError when dimensions mismatch."""
    x_train = pd.DataFrame({'feature1': [1, 2, 3]})
    y_train = pd.Series(['Good', 'Bad']) # Missing one label
    
    # Expect a ValueError
    with pytest.raises(ValueError):
        train_logistic_regression(x_train, y_train)


def test_train_logistic_regression_reproducibility():
    """Test if setting random_state yields identical models."""
    x_train = pd.DataFrame({'f1': [1, 2, 3, 4], 'f2': [0.1, 0.2, 0.3, 0.4]})
    y_train = pd.Series(['Good', 'Bad', 'Good', 'Bad'])

    model1 = train_logistic_regression(x_train, y_train, random_state=42)
    model2 = train_logistic_regression(x_train, y_train, random_state=42)

    assert (model1.coef_ == model2.coef_).all(), "Models with the same random_state must have identical coefficients."


def test_train_logistic_regression_parameters():
    """Test if custom parameters like max_iter are correctly applied."""
    x_train = pd.DataFrame({'feature1': [1, 2, 3, 4]})
    y_train = pd.Series(['Good', 'Bad', 'Good', 'Bad'])

    custom_iter = 777
    model = train_logistic_regression(x_train, y_train, max_iter=custom_iter)
    assert model.max_iter == custom_iter, f"Expected max_iter to be {custom_iter}, but got {model.max_iter}."