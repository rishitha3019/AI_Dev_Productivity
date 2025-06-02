# etl/load.py
def load(df):
    df.to_csv('data/processed/processed_productivity.csv', index=False)
