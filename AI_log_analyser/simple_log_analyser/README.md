# Simple Log Analyser

A collection of Python scripts for detecting anomalies in log files by analyzing error patterns and frequency within time windows.

## Overview

The Simple Log Analyser provides three different approaches to analyze log files and detect anomalies based on error frequency thresholds. It focuses on identifying time periods with unusually high error rates that might indicate system issues or failures.

## Features

- **Log Parsing**: Automatically parses log files with timestamp, level, and message format
- **Time-based Analysis**: Groups logs into 30-second intervals for pattern detection
- **Anomaly Detection**: Identifies periods with error counts exceeding defined thresholds
- **Flexible Output**: Options for concise or detailed reporting
- **Pandas Integration**: Leverages pandas for efficient data manipulation and analysis

## Scripts

### 01_log_analyser.py
Basic anomaly detection script that:
- Parses log files using regex patterns
- Detects ERROR log spikes in 30-second windows
- Uses a threshold of 3 errors per 30-second interval
- Outputs concise anomaly alerts

**Usage:**
```bash
python 01_log_analyser.py <log_file_path>
```

### 02_log_analyser.py
Enhanced version with output options:
- All features from 01_log_analyser.py
- Interactive or command-line output format selection
- Concise output (option 1): Simple anomaly alerts
- Full output (option 2): Detailed log entries for each anomaly period

**Usage:**
```bash
# Interactive mode
python 02_log_analyser.py <log_file_path>

# Direct mode with output option
python 02_log_analyser.py <log_file_path> <output_option>
```

Where `<output_option>` is:
- `1` for concise output
- `2` for full log output with details

### 03_log_analyser.py
Simplified version with hardcoded file path:
- Uses a fixed log file path (`../app.log`)
- Automatically provides detailed output for all anomalies
- Improved log parsing for better handling of message content

**Usage:**
```bash
python 03_log_analyser.py
```

## Log Format Requirements

All scripts expect log files in the following format:
```
YYYY-MM-DD HH:MM:SS LEVEL MESSAGE
```

Example:
```
2024-01-15 10:30:45 ERROR Database connection failed
2024-01-15 10:30:46 INFO User login successful
2024-01-15 10:30:47 ERROR Authentication timeout
```

## Dependencies

- `pandas`: For data manipulation and analysis
- `sys`: For command-line argument handling
- `re`: For regex-based log parsing
- `collections.Counter`: For counting occurrences

Install dependencies:
```bash
pip install pandas
```

## Configuration

### Threshold Settings
The default threshold is set to 3 errors per 30-second window. You can modify this by changing the `threshold` variable in each script:

```python
threshold = 3  # Change this value as needed
```

### Time Window
The analysis uses 30-second time windows by default. This can be adjusted by modifying the floor operation:

```python
# Current: 30-second windows
error_count = Counter(df[df["level"] == "ERROR"]["timestamp"].dt.floor("30s"))

# Example: 1-minute windows
error_count = Counter(df[df["level"] == "ERROR"]["timestamp"].dt.floor("1min"))
```

## Output Examples

### Concise Output (Option 1)
```
Anomaly detected 5 ERROR logs in 30 seconds at 2024-01-15 10:30:30
Anomaly detected 4 ERROR logs in 30 seconds at 2024-01-15 10:31:00
```

### Full Output (Option 2)
```
-> Anomaly detected 5 ERROR logs in 30 seconds at 2024-01-15 10:30:30
    timestamp               level  message
0   2024-01-15 10:30:31     ERROR  Database connection failed
1   2024-01-15 10:30:33     ERROR  Authentication timeout
2   2024-01-15 10:30:35     ERROR  Service unavailable
3   2024-01-15 10:30:37     ERROR  Connection refused
4   2024-01-15 10:30:39     ERROR  Timeout occurred
################################################################################
```

## Use Cases

- **System Monitoring**: Detect unusual error patterns in real-time
- **Incident Detection**: Identify potential system failures or attacks
- **Performance Analysis**: Understand error distribution over time
- **Alerting**: Trigger notifications when error thresholds are exceeded
- **Log Analysis**: Quick overview of problematic time periods

## Limitations

- Only analyzes ERROR level logs
- Fixed time window of 30 seconds (configurable)
- Requires structured log format
- Basic regex parsing may not handle all log variations
- No persistent storage of analysis results

## Future Enhancements

- Support for multiple log levels
- Configurable time windows via command line
- JSON/CSV output formats
- Real-time log monitoring
- Machine learning-based anomaly detection
- Integration with alerting systems
