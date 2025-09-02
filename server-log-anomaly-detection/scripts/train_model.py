import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
from preprocess_logs import load_logs

def train_model():
    logs = load_logs("data/sample_syslog.csv")

    # Use "count" values for anomaly detection
    X = logs[['count']]

    # Train Isolation Forest
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(X)

    # Save model
    joblib.dump(model, "models/isolation_forest.pkl")
    print("✅ Model trained and saved at models/isolation_forest.pkl")

if __name__ == "__main__":
    train_model()
