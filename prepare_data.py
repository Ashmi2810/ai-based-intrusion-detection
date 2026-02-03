import pandas as pd

df = pd.read_csv("traffic.csv")

print("Original rows:", len(df))

# clean protocol text
df["protocol"] = df["protocol"].str.strip().str.upper()

# encode protocol
df["protocol"] = df["protocol"].map({
    "TCP": 0,
    "UDP": 1,
    "OTHER": 2
})

# remove IPs (not useful for first model)
df = df.drop(["src_ip", "dst_ip"], axis=1)

print("After cleaning rows:", len(df))
print(df.head())

df.to_csv("clean_data.csv", index=False)

df["timestamp"] = pd.to_datetime(df["timestamp"])

window = df.set_index("timestamp").rolling("60s")

df["packet_rate"] = window["length"].count()
df["avg_length"] = window["length"].mean()

