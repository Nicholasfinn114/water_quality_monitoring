import pandas as pd

class WaterQualityEvaluator:
    """Evaluates water quality based on pH and turbidity thresholds."""
    def __init__(self, ph_min=6.5, ph_max=8.5, turbidity_max=1.0):
        self.ph_min, self.ph_max = ph_min, ph_max
        self.turbidity_max = turbidity_max

    def _evaluate_row(self, row):
        """Internal helper to evaluate a single row."""
        reasons = []
        if pd.isna(row['ph']): reasons.append("missing pH")
        elif not (self.ph_min <= row['ph'] <= self.ph_max): reasons.append("pH too low" if row['ph'] < self.ph_min else "pH too high")

        if pd.isna(row['turbidity']): reasons.append("missing turbidity")
        elif row['turbidity'] > self.turbidity_max: reasons.append("turbidity too high")

        return (not reasons), (", ".join(reasons) or "Safe")

    def evaluate_dataframe(self, df):
        """Evaluates DataFrame, adding 'is_safe' and 'safety_reason' columns."""
        if df is None: return None
        df[['is_safe', 'safety_reason']] = df.apply(self._evaluate_row, axis=1, result_type='expand')
        return df
