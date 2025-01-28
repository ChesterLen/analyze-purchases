import pandas as pd

data = pd.read_csv('../sales_data.csv')

df = pd.DataFrame(data)

df_isnull = df.isnull().any().any()

if df_isnull:
    print("Missing values detected. Replacing them with NaN (if needed).")
    df = df.fillna('None')

df_duplicates = df.duplicated().sum()

if df_duplicates > 0:
    print(f"Found {df_duplicates} duplicate rows. Removing duplicates.")
    df = df.drop_duplicates()
