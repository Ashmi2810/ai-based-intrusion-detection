import pandas as pd

df = pd.read_csv("traffic.csv")

print("Total packets:", len(df))
print("\nProtocol counts:")
print(df["protocol"].value_counts())

print("\nTop destination ports:")
print(df["dst_port"].value_counts().head(10))
