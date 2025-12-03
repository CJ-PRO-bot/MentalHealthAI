import pandas as pd     #read, clean, dataframe, etc..
from pathlib import Path #makes the path object, no need to manually write path as D:/folder1/folder2... instead as 'path'
from .utils import get_data_path  

def load_raw_data(fname):  #reads data from raw CSV
    path = get_data_path("raw") / fname
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path)

def inspect_data(df):  #prints head, info, and mmissing values so i can understand dataset
    print(df.head())
    print(df.info())
    print(df.isna().sum())   #sum of empty values(isna-Is not avalailable)

def basic_cleaning(df):  #trims column names and removes empty rows/columns
    df = df.rename(columns=lambda x: x.strip()) #rename column in dataframe, and for every column in x, remove leading and ending spaces(eg. " gg "-> "gg")
    df = df.dropna(axis=1, how="all")  #remove empty columns, if codition all values in column is empty/NaN
    df = df.dropna(axis=0, how="all")  #rows
    return df

def save_processed(df, fname):  #saves the cleaned data/df into processed folder
    out = get_data_path("processed") / fname
    df.to_csv(out, index=False)  #index is false to avoid pandas from creating extra column
    print("Saved:", out)   #message where file is saved
    return out

###MAIN PIPELINE ####
def run_data_loading(raw_filename, processed_filename):  ###main pipeline, loads, inspect, clean, save, return
    df = load_raw_data(raw_filename)  #loads data from data/raw and stores in df
    inspect_data(df)   #prints important info about the first 5 rows, giving overall view of raw data
    df_clean = basic_cleaning(df)  #cleans the df using the function earlier
    save_processed(df_clean, processed_filename)  #saves cleaned data in the processed folder
    return df_clean
