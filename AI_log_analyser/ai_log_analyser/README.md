# AI Log Analyzer

A Python-based intelligent log analysis tool that uses machine learning to detect anomalies in application logs. This project leverages Isolation Forest algorithm to identify unusual patterns in log data based on log levels and message characteristics.

## Features

- **Automated Log Parsing**: Processes structured log files with timestamp, level, and message extraction
- **Anomaly Detection**: Uses Isolation Forest algorithm to detect unusual log entries
- **Multi-feature Analysis**: Analyzes logs based on:
  - Log level severity (INFO, WARNING, ERROR, CRITICAL)
  - Message length patterns
- **Structured Output**: Provides clear identification of anomalous log entries
- **Configurable Sensitivity**: Adjustable contamination parameter for fine-tuning detection

## Technology Stack

- **Python 3.x**
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning (Isolation Forest)
- **NumPy**: Numerical operations (via dependencies)

## Prerequisites

- Python 3.6 or higher
- pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abcofdevops/aiops.git
cd aiops/AI_log_analyser/ai_log_analyser
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
ai_log_analyser/
├── ai_log_analyser.py    # Main analysis script
├── requirements.txt      # Dependencies
├── ../app.log            # Sample log file (expected format)
└── README.md             # This file
```

## Log Format

The analyzer expects log files with the following format:
```
TIMESTAMP LEVEL MESSAGE
```

**Example:**
```
2024-01-15 10:30:25 INFO Application started successfully
2024-01-15 10:30:26 WARNING Database connection timeout
2024-01-15 10:30:27 ERROR Failed to process user request
2024-01-15 10:30:28 CRITICAL System out of memory
```

**Supported Log Levels:**
- `INFO` (Score: 1)
- `WARNING` (Score: 2) 
- `ERROR` (Score: 3)
- `CRITICAL` (Score: 4)

## Usage

### Basic Usage

1. Place your log file in the same directory as the script or update the file path:
```python
log_file_path = "../app.log"  # Update with your file path
```

2. Run the analyzer:
```bash
python ai_log_analyser.py
```

3. View the detected anomalies in the output

### Customization

#### Adjust Sensitivity
Modify the contamination parameter in the script:
```python
model = IsolationForest(contamination=0.1, random_state=42)
```
- **Lower values** (e.g., 0.05): More sensitive, detects more anomalies
- **Higher values** (e.g., 0.2): Less sensitive, detects fewer anomalies

#### Change Log File Path
Update the file path variable:
```python
log_file_path = "/path/to/your/logfile.log"
```

## How It Works

### 1. Log Parsing
The script reads the log file and extracts:
- **Timestamp**: Date and time of the log entry
- **Level**: Log severity level
- **Message**: The actual log message

### 2. Feature Engineering
Two key features are created for analysis:
- **Level Score**: Numeric representation of log severity
- **Message Length**: Character count of the log message

### 3. Anomaly Detection
Uses the Isolation Forest algorithm to:
- Train on the extracted features
- Identify outliers that deviate from normal patterns
- Flag entries as "Anomaly" or "Normal"

### 4. Results
Displays only the detected anomalies with:
- Original timestamp
- Log level
- Message content
- Feature scores
- Anomaly classification

## Algorithm Details

**Isolation Forest** is chosen for its effectiveness in:
- **Unsupervised Learning**: No need for labeled training data
- **Efficiency**: Fast processing of large datasets
- **Robustness**: Handles outliers effectively
- **Scalability**: Works well with varying data sizes

The algorithm isolates anomalies by:
1. Randomly selecting features
2. Randomly selecting split values
3. Creating isolation trees
4. Measuring path lengths to isolate data points
5. Shorter paths indicate anomalies

## Configuration Options

### Model Parameters
```python
IsolationForest(
    contamination=0.1,      # Expected proportion of anomalies
    random_state=42,        # For reproducible results
    n_estimators=100,       # Number of isolation trees (default)
    max_samples='auto',     # Number of samples to train each tree (default)
    max_features=1.0        # Number of features to train each tree (default)
)
```

### Log Level Mapping
```python
level_mapping = {
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3,
    "CRITICAL": 4
}
```

## Example Output

```
**Detected Anomalies:**
        timestamp level                    message                              level_score  message_length anomaly is_anomaly
15  2024-01-15 14:23:45  ERROR     Database connection failed after 30 seconds        3              47       -1      Anomaly
23  2024-01-15 15:45:12  CRITICAL  System memory usage exceeded 95%                   4              33       -1      Anomaly
31  2024-01-15 16:12:30  WARNING   Unusual spike in API response time: 5000ms         2              51       -1      Anomaly
```

## Testing

### Sample Log Generation
Create a test log file with mixed normal and anomalous entries:

```bash
# Create sample log file
cat > test.log << EOF
2024-01-15 10:00:01 INFO Application started
2024-01-15 10:00:02 INFO User logged in
2024-01-15 10:00:03 WARNING High memory usage
2024-01-15 10:00:04 ERROR Database connection failed
2024-01-15 10:00:05 CRITICAL System shutdown initiated
2024-01-15 10:00:06 INFO Normal operation resumed
EOF
```

### Validation
1. Run the analyzer on the sample data
2. Verify that unusual patterns are detected
3. Adjust contamination parameter if needed

## Troubleshooting

### Common Issues

1. **File Not Found Error**
   ```
   FileNotFoundError: [Errno 2] No such file or directory: '../app.log'
   ```
   **Solution**: Update the `log_file_path` variable with the correct path

2. **No Anomalies Detected**
   - **Cause**: Contamination parameter too low or uniform log patterns
   - **Solution**: Increase contamination value or check log data variety

3. **Import Errors**
   ```
   ModuleNotFoundError: No module named 'pandas'
   ```
   **Solution**: Install required packages:
   ```bash
   pip install -r requirements.txt
   pip install pandas scikit-learn
   ```

4. **Log Format Issues**
   - **Cause**: Logs don't match expected format
   - **Solution**: Ensure logs follow `TIMESTAMP LEVEL MESSAGE` format

## Performance Considerations

- **Memory Usage**: Proportional to log file size
- **Processing Time**: O(n log n) where n is number of log entries
- **Scalability**: Suitable for files up to several GB
- **Optimization**: For very large files, consider batch processing

## Future Enhancements

### Planned Features
- [ ] **Real-time Log Monitoring**: Stream processing capabilities
- [ ] **Multiple Log Formats**: Support for JSON, CSV, and custom formats
- [ ] **Advanced Features**: Include timestamp patterns, error codes
- [ ] **Visualization**: Charts and graphs for anomaly trends
- [ ] **Alerting**: Email/SMS notifications for critical anomalies
- [ ] **Configuration File**: External config for parameters
- [ ] **Batch Processing**: Handle multiple log files
- [ ] **Export Results**: Save anomalies to CSV/JSON

### Potential Improvements
- **Feature Engineering**: Add more sophisticated features
- **Model Ensemble**: Combine multiple algorithms
- **Temporal Analysis**: Consider time-based patterns
- **Clustering**: Group similar anomalies
- **Baseline Learning**: Establish normal behavior patterns

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Development Guidelines
- Follow PEP 8 coding standards
- Add comments for complex logic
- Test with various log formats
- Document new features

## License

This project is part of the AIOps repository. Please refer to the main repository for licensing information.

## Acknowledgments

- **Scikit-learn**: For the Isolation Forest implementation
- **Pandas**: For efficient data manipulation
- **AIOps Community**: For the collaborative development environment

## Support

- **Issues**: [GitHub Issues](https://github.com/abcofdevops/aiops/issues)
- **Repository**: [AIOps Main Repository](https://github.com/abcofdevops/aiops)

---

**Part of the AIOps (AI for IT Operations) Project**
