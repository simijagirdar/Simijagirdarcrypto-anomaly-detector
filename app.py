import streamlit as st
import pandas as pd

st.title("Crypto Anomaly Detector")

uploaded_file = st.file_uploader("Upload your transaction CSV")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of uploaded data:", df)

    # Placeholder logic
    st.write("Anomaly Score: 72.3%")
