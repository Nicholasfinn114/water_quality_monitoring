import os
import pandas as pd
from .load_data import load_data
from .clean_data import clean_data
from .evaluate import WaterQualityEvaluator

def run_pipeline(filepath, output_filepath=None, location_filter=None):
    """Runs the water quality monitoring pipeline."""
    df = load_data(filepath)
    if df is None: return

    df = clean_data(df)
    if df is None: return

    if location_filter:
        df = df[df['location'].str.contains(location_filter, case=False, na=False)]
        if df.empty:
            print(f"No data for '{location_filter}'.")
            return

    evaluator = WaterQualityEvaluator()
    df = evaluator.evaluate_dataframe(df)
    if df is None: return

    # Print results as per expected output
    for _, row in df.iterrows():
        status = "✅ Safe" if row['is_safe'] else "❌ Unsafe"
        reason = "" if row['is_safe'] else f" ({row['safety_reason']})"
        print(f"Sensor {int(row['sensor_id'])} at {row['location']}: {status}{reason}")

   

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    project_root = os.path.join(current_dir, '..')
    data_filepath = os.path.join(project_root, 'data', 'sensor_data.csv')
    results_output_filepath = os.path.join(project_root, 'results.csv')

    run_pipeline(data_filepath, results_output_filepath)
    # run_pipeline(data_filepath, location_filter="Lake C") # Example for bonus filter
