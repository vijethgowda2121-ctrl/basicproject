import streamlit as st

from utils.preprocessing import preprocess
from utils.model_utils import train_model

st.title("🤖 Machine Learning")

if "data" not in st.session_state:

    st.warning("Upload dataset first")
    st.stop()

df = st.session_state["data"]

target = st.selectbox(
    "Select Target Column",
    df.columns
)

if st.button("Train Model"):

    processed = preprocess(df)

    model, score, task = train_model(
        processed,
        target
    )

    st.session_state["model"] = model
    st.session_state["processed"] = processed
    st.session_state["target"] = target

    st.success(f"{task} Model Trained")

    if task == "Classification":
        st.metric("Accuracy", f"{score:.4f}")
    else:
        st.metric("R² Score", f"{score:.4f}")

    importance = model.feature_importances_

    features = processed.drop(
        columns=[target]
    ).columns

    import pandas as pd

    fi = pd.DataFrame({
        "Feature":features,
        "Importance":importance
    })

    fi = fi.sort_values(
        "Importance",
        ascending=False
    )

    st.bar_chart(
        fi.set_index("Feature")
    )
