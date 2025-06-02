import pandas as pd

def extract():
    df = pd.read_csv('data/raw/AI_dev_productivity.csv')
    return df
