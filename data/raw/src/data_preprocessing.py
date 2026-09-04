
import pandas as pd

def load_data():
    inflation = pd.read_csv('data/raw/inflation.csv')
    house_prices = pd.read_csv('data/raw/house_prices.csv')
    return inflation, house_prices

def clean_inflation(df):
    df.columns = df.columns.str.strip()
    df = df.dropna()
    return df

def clean_house_prices(df):
    df.columns = df.columns.str.strip()
    df = df.dropna()
    return df
