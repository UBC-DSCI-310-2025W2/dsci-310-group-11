import pandas as pd

def generate_quality_label(data, threshold = 6):
    """
    Generates a new column in wine datasets that creates a categorical label based on quality
    
    Parameters
    ----------
    data : pandas.DataFrame
        The input DataFrame with 'quality' column for transforming
    threshold : int, optional
        Positive integer threshold above which wine will be labelled 'Good'
        
    Returns
    -------
    pandas.DataFrame
        A dataframe containing a new 'label' column
        
    Raises
    ------
    KeyError
        If 'quality' column is missing or does not exist
    ValueError
        If threshold is negative
    TypeError
        If threshold is not an integer.
    TypeError
        If df is not a pandas DataFrame.
    
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")

    if not isinstance(threshold, int):
        raise TypeError("threshold must be an integer")
    if threshold <= 0:
        raise ValueError("threshold must be positive")

    if "quality" not in data.columns:
        raise KeyError("The dataframe must contain a 'quality' column")
    

    
    labeled_data = data.copy()
    labeled_data["label"] = labeled_data["quality"].apply(
        lambda x: "Good" if x >= threshold else "Bad"
    )
    return labeled_data