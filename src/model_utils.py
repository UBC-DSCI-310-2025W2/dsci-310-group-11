# src/model_utils.py

from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

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
    random_state : int or None, optional
        Used when shuffling the data, by default None.    
        
    Returns
    -------
    sklearn.linear_model.LogisticRegression
        A fitted Logistic Regression model.
        
    Raises
    ------
    TypeError
        If x_train is not a pandas DataFrame or numpy ndarray.
    TypeError
        If y_train is not a pandas Series or numpy ndarray.
    TypeError
        If max_iter is not an integer.
    TypeError
        If random_state is not an integer or None.
    ValueError
        If x_train or y_train is empty.
    ValueError
        If max_iter is not a positive integer.
    ValueError
        If the number of samples in x_train and y_train do not match.
    """
    if not isinstance(x_train, (pd.DataFrame, np.ndarray)):
        raise TypeError("x_train must be a pandas DataFrame or numpy ndarray.")

    if not isinstance(y_train, (pd.Series, np.ndarray)):
        raise TypeError("y_train must be a pandas Series or numpy ndarray.")

    if not isinstance(max_iter, int):
        raise TypeError("max_iter must be an integer.")

    if random_state is not None and not isinstance(random_state, int):
        raise TypeError("random_state must be an integer or None.")

    if len(x_train) == 0 or len(y_train) == 0:
        raise ValueError("x_train and y_train must not be empty.")

    if max_iter <= 0:
        raise ValueError("max_iter must be a positive integer.")

    if len(x_train) != len(y_train):
        raise ValueError("x_train and y_train must have the same number of rows.")
    
    model = LogisticRegression(max_iter=max_iter, random_state=random_state)
    model.fit(x_train, y_train)
    
    return model