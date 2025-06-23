import pandas as pd
from collections import Counter

# Read log file
log_file_path = "../app.log"  # Update with your file path if needed
with open(log_file_path, "r") as file:
    logs = file.readlines()

# Parse logs into a structured DataFrame
data = []
for log in logs:
    parts = log.strip().split(" ", 3)  # Ensure the message part is captured fully
    if len(parts) < 4:
        continue  # Skip malformed lines
    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = parts[3]
    data.append([timestamp, level, message])

df = pd.DataFrame(data, columns=["timestamp", "level", "message"])

# Convert timestamp to datetime format for sorting
df["timestamp"] = pd.to_datetime(df["timestamp"])

error_count = Counter(df[df["level"] == "ERROR"]["timestamp"].dt.floor("30s"))

threshold = 3

for time, count in error_count.items(): 
    if count > threshold:
        print(f"-> Anomaly detected {count} ERROR logs in 30 seconds at {time}")
        print(df[df["timestamp"].dt.floor("30s") == time])
        print("#"*80)
