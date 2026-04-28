import pandas as pd

def load_energy_data(filepath):
    df = pd.read_csv(filepath)
    print("COLUMNS READ BY PANDAS:", list(df.columns))
    df.columns = df.columns.str.strip()
    df['Date'] = pd.to_datetime(df['Date'])
    return df
