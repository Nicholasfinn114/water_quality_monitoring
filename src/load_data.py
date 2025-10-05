# src/load_data.py

import pandas as pd

def load_data(filepath):
    """Loads CSV into DataFrame."""
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
