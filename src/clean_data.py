
import pandas as pd

def clean_data(df):
    """Cleans sensor data: converts to numeric, preserves NaNs for evaluation."""
    if df is None: return None
    df[['ph', 'turbidity', 'temperature']] = df[['ph', 'turbidity', 'temperature']].apply(pd.to_numeric, errors='coerce')
    return df
