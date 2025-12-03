import pandas as pd
from sklearn.preprocessing import StandardScaler
from .utils import get_data_path

def load_processed(name):
    path = get_data_path("processed") / name
    return pd.read_csv(path)

def convert_dtypes(df):
    if "YEAR (DISPLAY)" in df.columns:
        df["YEAR"] = pd.to_numeric(df["YEAR (DISPLAY)"], errors="coerce")
    for col in ["Value", "Low", "High", "Numeric"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

def filter_bhutan(df):
    if "COUNTRY (CODE)" in df.columns:
        df = df[df["COUNTRY (CODE)"] == "BTN"]
    return df

def handle_missing(df):
    df = df.dropna(subset=["YEAR"])
    if "Value" in df.columns:
        df = df.dropna(subset=["Value"])
    return df

def encode(df):
    if "GHO (CODE)" in df.columns:
        df["indicator_code"] = df["GHO (CODE)"].astype("category").cat.codes
    if "DIMENSION (TYPE)" in df.columns:
        df["dim_type_code"] = df["DIMENSION (TYPE)"].astype("category").cat.codes
    return df

def scale(df):
    sc = StandardScaler()
    df["Value_scaled"] = sc.fit_transform(df[["Value"]])
    return df, sc

def select_features(df):
    cols = [c for c in ["YEAR", "Value", "Value_scaled", "indicator_code", "dim_type_code"] if c in df.columns]
    return df[cols]

def run_preprocessing(input_file, output_file):
    df = load_processed(input_file)
    df = convert_dtypes(df)
    df = filter_bhutan(df)
    df = handle_missing(df)
    df = encode(df)
    df, _ = scale(df)
    df_final = select_features(df)
    out = get_data_path("processed") / output_file
    df_final.to_csv(out, index=False)
    print("Saved:", out)
    return df_final
