import streamlit as st

st.title("Crypto Anomaly Detector")

# Input wallet address
wallet_address = st.text_input("Enter crypto wallet address")

if st.button("Check for anomalies"):
    if wallet_address:
        # Placeholder: Later we’ll connect to an API
        st.write(f"Analyzing wallet: `{wallet_address}`")

        # Simulated result
        st.success("Anomaly Score: 72.3%")
        st.info("Suspicious activity detected in 3 of the last 50 transactions.")
    else:
        st.warning("Please enter a valid wallet address.")
