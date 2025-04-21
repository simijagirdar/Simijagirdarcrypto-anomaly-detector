 import streamlit as st
import requests
import pandas as pd

st.title("Crypto Anomaly Detector")

# --- Replace this with your actual API key ---
ETHERSCAN_API_KEY = "IB87PTRDRG5UARKMFM8CFF5Q6SBYBSJ7E8"

# --- Function to fetch transactions ---
def fetch_transactions(wallet_address, api_key):
    url = (
        f"https://api.etherscan.io/api"
        f"?module=account"
        f"&action=txlist"
        f"&address={wallet_address}"
        f"&startblock=0"
        f"&endblock=99999999"
        f"&sort=desc"
        f"&apikey={api_key}"
    )
    response = requests.get(url)
    data = response.json()
    return data

# --- UI ---
wallet_address = st.text_input("Enter Ethereum wallet address")

if st.button("Check for anomalies"):
    if wallet_address:
        with st.spinner("Fetching transaction data..."):
            data = fetch_transactions(wallet_address, ETHERSCAN_API_KEY)
        
        if data["status"] == "1":
            tx_list = data["result"]
            df = pd.DataFrame(tx_list)

            if not df.empty:
                st.success(f"Fetched {len(df)} transactions.")
                df["value"] = df["value"].astype(float) / 1e18  # Convert from Wei to ETH
                df["timeStamp"] = pd.to_datetime(df["timeStamp"], unit='s')
                st.dataframe(df[["hash", "from", "to", "value", "timeStamp"]].head(10))
                st.info("Anomaly detection logic coming soon!")
            else:
                st.warning("No transactions found for this wallet.")
        else:
            st.error("Failed to fetch data. Check wallet address or API key.")
    else:
        st.warning("Please enter a wallet address.")
