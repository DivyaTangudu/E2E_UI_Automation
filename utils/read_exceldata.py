import pandas as pd

# Read Excel and convert to list of dicts
def read_excel_data(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict("records")