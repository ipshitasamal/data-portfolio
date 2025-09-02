# 🔍 Server Log Anomaly Detection

This project detects anomalies in server logs (e.g., traffic spikes, unusual activity) using **Isolation Forest**.

## 🚀 Tech Stack
- Python
- Pandas
- Scikit-learn
- Joblib

## 📂 Project Structure

## ▶️ How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Preprocess data
python scripts/preprocess_logs.py

# Train model
python scripts/train_model.py

# Evaluate model
python scripts/evaluate_model.py

# Detect anomalies
python scripts/detect_anomalies.py

🚨 Detected anomalies:
              timestamp  count  anomaly
123  1995-07-01 01:12:00   2200      -1
456  1995-07-01 04:30:00   3000      -1
...
