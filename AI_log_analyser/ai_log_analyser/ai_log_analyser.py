import pandas as pd
from sklearn.ensemble import IsolationForest

log_file_path = "../app.log"  # Update with your file path if needed
with open(log_file_path, "r") as file:
    logs = file.readlines()

data = []
for log in logs:
    parts = log.strip().split(" ", 3)
    if len(parts) < 4:
        continue
    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = parts[3]
    data.append([timestamp, level, message])

df = pd.DataFrame(data, columns=["timestamp", "level", "message"])
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Assign numeric scores to log levels
level_mapping = {"INFO": 1, "WARNING": 2, "ERROR": 3, "CRITICAL": 4}
df["level_score"] = df["level"].map(level_mapping)

# Add message length as a new feature
df["message_length"] = df["message"].apply(len)

# AI Model for Anomaly Detection (Isolation Forest)
model = IsolationForest(contamination=0.1, random_state=42)  # Lower contamination for better accuracy
df["anomaly"] = model.fit_predict(df[["level_score", "message_length"]])

# Mark anomalies in a readable format
df["is_anomaly"] = df["anomaly"].apply(lambda x: "Anomaly" if x == -1 else "Normal")

#Print only detected anomalies
anomalies = df[df["is_anomaly"] == "Anomaly"]
print("\n **Detected Anomalies:**\n", anomalies)

#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#    print("\n **Detected Anomalies:**\n", anomalies)
