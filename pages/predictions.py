import streamlit as st
import pandas as pd

st.title("🔮 Predictions")

if "model" not in st.session_state:

    st.warning("Train model first")
    st.stop()

model = st.session_state["model"]

target = st.session_state["target"]

df = st.session_state["processed"]

features = df.drop(columns=[target])

inputs = {}

for col in features.columns:

    inputs[col] = st.number_input(
        col,
        value=float(features[col].mean())
    )

if st.button("Predict"):

    sample = pd.DataFrame([inputs])

    prediction = model.predict(sample)

    st.success(
        f"Prediction: {prediction[0]}"
    )
