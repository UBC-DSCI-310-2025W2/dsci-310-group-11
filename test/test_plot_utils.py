import pytest
import pandas as pd
from src.plot_utils import create_quality_boxplot


def test_create_quality_boxplot_success():
    """Test if the function successfully returns a plot axes object."""
    df = pd.DataFrame({
        "label": ["Good", "Bad", "Good", "Bad"],
        "alcohol": [10.5, 9.2, 11.1, 8.9]
    })

    ax = create_quality_boxplot(df)
    assert ax is not None, "Function should return a plot axes object."


def test_create_quality_boxplot_custom_y_label():
    """Test if the function works with another numeric column."""
    df = pd.DataFrame({
        "label": ["Good", "Bad", "Good", "Bad"],
        "pH": [3.2, 3.4, 3.1, 3.5]
    })

    ax = create_quality_boxplot(df, y_col="pH")
    assert ax is not None, "Function should return a plot axes object."


def test_create_quality_boxplot_handles_missing_values():
    """Test if the function works when y column contains missing values."""
    df = pd.DataFrame({
        "label": ["Good", "Bad", "Good", "Bad"],
        "alcohol": [10.5, None, 11.1, 8.9]
    })

    ax = create_quality_boxplot(df)
    assert ax is not None, "Function should still return a plot axes object."


def test_create_quality_boxplot_type_error():
    """Test if non-DataFrame input raises TypeError."""
    with pytest.raises(TypeError):
        create_quality_boxplot("not_a_dataframe")


def test_create_quality_boxplot_value_error():
    """Test if missing y column raises ValueError."""
    df = pd.DataFrame({
        "label": ["Good", "Bad", "Good", "Bad"],
        "sugar": [1, 2, 3, 4]
    })

    with pytest.raises(ValueError):
        create_quality_boxplot(df)