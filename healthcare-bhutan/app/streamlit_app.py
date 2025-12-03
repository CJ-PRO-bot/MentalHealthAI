import streamlit as st
import pandas as pd
from src.utils import get_data_path

st.title("Bhutan Health Indicators – Demo App")

path = get_data_path("processed") / "health_indicators_preprocessed.csv"
if not path.exists():
    st.error("Run preprocessing first.")
else:
    df = pd.read_csv(path)
    st.write("Preview:", df.head())
    st.line_chart(df.groupby("YEAR")["Value"].mean())
