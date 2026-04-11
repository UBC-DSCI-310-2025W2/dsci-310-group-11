import pytest
import sys
import os
import pandas as pd
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_wrangling import generate_quality_label

def test_data_wrangling_success():
    """Test that generate_quality_label returns a DataFrame with correct labels using the default threshold of 6."""
    raw_data = pd.DataFrame({'quality': [3,7,5,3,9,8]})

    wrangled_data = generate_quality_label(raw_data, 6)
    assert isinstance(wrangled_data, pd.DataFrame), "wrangled should be a pd.DataFrame."
    assert list(wrangled_data["label"]) == ["Bad", "Good", "Bad", "Bad", "Good", "Good"]

def test_data_wrangling_success_diff_threshold():
    """Test that generate_quality_label correctly re-labels wines when a non-default threshold is supplied."""
    raw_data = pd.DataFrame({'quality': [3,7,5,3,9,8]})

    wrangled_data = generate_quality_label(raw_data, 4)
    assert isinstance(wrangled_data, pd.DataFrame), "wrangled should be a pd.DataFrame."
    assert list(wrangled_data["label"]) == ["Bad", "Good", "Good", "Bad", "Good", "Good"]

def test_data_wrangling_value_error():
    """Test if negative threshold raises ValueError"""
    raw_data = pd.DataFrame({'quality': [3,7,5,3,9,8]})

    with pytest.raises(ValueError):
        generate_quality_label(raw_data, -2)

def test_data_wrangling_type_error_threshold():
    """Test if non-int threshold raises ValueError"""
    raw_data = pd.DataFrame({'quality': [3,7,5,3,9,8]})

    with pytest.raises(TypeError):
        generate_quality_label(raw_data, 3.5)

def test_data_wrangling_type_error_dataframe():
    """Test if non-dataframe data raises ValueError"""
    raw_data = [3,7,5,3,9,8]

    with pytest.raises(TypeError):
        generate_quality_label(raw_data, 6)

def test_data_wrangling_key_error_dataframe():
    """Test if non-dataframe data raises ValueError"""
    raw_data = pd.DataFrame({'acidity': [3,7,5,3,9,8]})

    with pytest.raises(KeyError):
        generate_quality_label(raw_data, 6)