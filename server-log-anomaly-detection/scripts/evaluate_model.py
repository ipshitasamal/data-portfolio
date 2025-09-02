import pandas as pd
import joblib
from preprocess_logs import load_logs
from sklearn.metrics import classification_report

def evaluate_model():
    logs = load_logs("data/sample_syslog.csv")
    X = logs[['count']]

    # Load trained model
    model = joblib.load("models/isolation_forest.pkl")

    # Predict anomalies (-1 = anomaly, 1 = normal)
    predictions = model.predict(X)
    logs['anomaly'] = predictions

    # Just for demonstration, let's mark top 5% counts as anomalies (ground truth)
    threshold = logs['count'].quantile(0.95)
    logs['true_anomaly'] = (logs['count'] > threshold).astype(int)

    # Convert model predictions to 0/1 for comparison
    logs['predicted_anomaly'] = (logs['anomaly'] == -1).astype(int)

    print("Classification Report:")
    print(classification_report(logs['true_anomaly'], logs['predicted_anomaly']))

if __name__ == "__main__":
    evaluate_model()
