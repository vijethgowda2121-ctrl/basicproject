import streamlit as st

from utils.visualization import (
    histogram,
    boxplot,
    correlation_heatmap
)

st.title("📈 Exploratory Data Analysis")

if "data" not in st.session_state:

    st.warning("Upload dataset first")
    st.stop()

df = st.session_state["data"]

numeric_cols = df.select_dtypes(
    include="number"
).columns

column = st.selectbox(
    "Select Numeric Column",
    numeric_cols
)

st.plotly_chart(
    histogram(df,column),
    use_container_width=True
)

st.plotly_chart(
    boxplot(df,column),
    use_container_width=True
)

st.plotly_chart(
    correlation_heatmap(df),
    use_container_width=True
)
