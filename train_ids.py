import pandas as pd
from sklearn.ensemble import IsolationForest

# load cleaned data
df = pd.read_csv("clean_data.csv")

print("Training data shape:", df.shape)

# features
X = df[["protocol", "src_port", "dst_port", "length"]]

# train model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

# anomaly prediction
df["anomaly"] = model.predict(X)
df["anomaly_score"] = model.decision_function(X)

print(df["anomaly"].value_counts())

# -------- DYNAMIC THRESHOLDING --------

scores = df["anomaly_score"]

rolling_mean = scores.rolling(window=100, min_periods=1).mean()
rolling_std = scores.rolling(window=100, min_periods=1).std()

df["severity"] = "Low"

df.loc[scores < rolling_mean - 2 * rolling_std, "severity"] = "Medium"
df.loc[scores < rolling_mean - 3 * rolling_std, "severity"] = "High"

# -------------------------------------

# save results
df.to_csv("ids_output.csv", index=False)

print("Model training complete. Results saved to ids_output.csv")
