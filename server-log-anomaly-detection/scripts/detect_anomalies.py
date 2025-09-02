import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
import joblib

# Load processed logs
df = pd.read_csv("data/processed_logs.csv")

# Detect which time column to use
time_col = None
for col in ["timestamp", "minute", "time", "date"]:
    if col in df.columns:
        time_col = col
        break

if not time_col:
    raise ValueError("❌ No time column found in dataset (expected: 'timestamp' or 'minute').")

# Train Isolation Forest
model = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = model.fit_predict(df[['count']])

# Save the trained model
joblib.dump(model, "models/isolation_forest.pkl")

# Show anomalies
print("🚨 Detected anomalies:")
print(df[df['anomaly'] == -1])

# Plot anomalies
plt.figure(figsize=(10,6))
plt.plot(df[time_col], df['count'], label="Log Count", color="blue")
plt.scatter(
    df.loc[df['anomaly'] == -1, time_col],
    df.loc[df['anomaly'] == -1, 'count'],
    color="red", label="Anomaly"
)
plt.xlabel("Time")
plt.ylabel("Log Count")
plt.title("Server Log Anomaly Detection")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
