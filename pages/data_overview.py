import streamlit as st
from utils.data_loader import load_data

st.title("📁 Dataset Overview")

file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx"]
)

if file:

    df = load_data(file)

    st.session_state["data"] = df

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Rows", len(df))
    c2.metric("Columns", len(df.columns))
    c3.metric("Missing", df.isna().sum().sum())
    c4.metric("Duplicates", df.duplicated().sum())

    st.dataframe(df.head())
