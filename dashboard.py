import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="ML-based IDS Dashboard", layout="wide")
st.title("🚨 Real-Time Intrusion Detection System")
st.write("Anomaly-based IDS using Machine Learning")


st.sidebar.header("Controls")
refresh_rate = st.sidebar.slider(
    "Auto-refresh (seconds)", 5, 60, 10
)


# Load IDS output
time.sleep(refresh_rate)
df = pd.read_csv("ids_final_output.csv")


# Metrics
total_packets = len(df)
anomalies = len(df[df["anomaly"] == -1])

col1, col2 = st.columns(2)
col1.metric("Total Packets", total_packets)
col2.metric("Detected Anomalies", anomalies)

st.divider()


st.subheader("Severity Distribution")

severity_counts = df[df["anomaly"] == -1]["severity"].value_counts()
st.bar_chart(severity_counts)


st.subheader("Detected Anomalies")

st.dataframe(
    df[df["anomaly"] == -1][
        ["protocol", "src_port", "dst_port", "length", "anomaly_score", "severity"]
    ]
)

