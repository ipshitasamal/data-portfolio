import pandas as pd

def load_logs(file_path):
    logs = pd.read_csv(file_path)
    # If there's no timestamp column, aggregate by minute index
    logs['minute'] = pd.to_datetime(logs.index, unit='s', origin='unix', errors='coerce')
    df = logs.groupby(logs['minute'].dt.floor('T')).size().reset_index(name='count')
    return df

if __name__ == "__main__":
    df = load_logs("data/sample_syslog.csv")
    # Save processed logs
    df.to_csv("data/processed_logs.csv", index=False)
    print("✅ Processed logs saved to data/processed_logs.csv")
    print(df.head())
