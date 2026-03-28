# src/model_utils.py

from sklearn.linear_model import LogisticRegression
import pandas as pd

def train_logistic_regression(x_train, y_train, max_iter=2000, random_state=None):
    """
    Trains a Logistic Regression model using the provided training data.
    
    Parameters
    ----------
    x_train : pandas.DataFrame or numpy.ndarray
        The feature matrix for training.
    y_train : pandas.Series or numpy.ndarray
        The target labels for training.
    max_iter : int, optional
        Maximum number of iterations taken for the solvers to converge, by default 2000.
    random_state : int, optional
        Used when shuffling the data, by default None.    
        
    Returns
    -------
    sklearn.linear_model.LogisticRegression
        A fitted Logistic Regression model.
        
    Raises
    ------
    ValueError
        If the number of samples in X_train and y_train do not match.
    """
    if len(x_train) != len(y_train):
        raise ValueError("X_train and y_train must have the same number of rows.")
    
    model = LogisticRegression(max_iter=max_iter, random_state=random_state)
    model.fit(x_train, y_train)
    
    return model