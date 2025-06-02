from etl.extract import extract
from etl.transform import transform
from etl.load import load

if __name__ == "__main__":
    df = extract()
    print("Columns in dataset:", df.columns.tolist())  
    df_transformed = transform(df)
    load(df_transformed)
    print("✅ ETL pipeline completed! Check data/processed/processed_productivity.csv")
