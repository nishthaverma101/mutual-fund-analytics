import pandas as pd
import os

DATA_FOLDER = "data/raw"

files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]

for file in files:

    print("\n" + "=" * 80)
    print(f"FILE: {file}")
    print("=" * 80)

    df = pd.read_csv(os.path.join(DATA_FOLDER, file)) #creates a data frame

    print("\nSHAPE:")
    print(df.shape) #gives number of rows and columns

    print("\nDATA TYPES:")
    print(df.dtypes)  #type of data types it contains

    print("\nFIRST 5 ROWS:")
    print(df.head()) #visualize the dataset

    print("\nMISSING VALUES:")
    print(df.isnull().sum())  #print missing value columns