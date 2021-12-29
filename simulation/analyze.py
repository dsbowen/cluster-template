import pandas as pd

DATA_FILE = "data/data.csv"

if __name__ == "__main__":
    print(pd.read_csv(DATA_FILE).head())
    