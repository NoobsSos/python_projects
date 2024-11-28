import pandas as pd

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_extreme_values(self):
        numeric_data = self.data.select_dtypes(include='number')
        if not numeric_data.empty:
            return numeric_data.describe().loc[['min', 'max']]
        else:
            print("No numeric data available for extreme values calculation.")
            return pd.DataFrame()