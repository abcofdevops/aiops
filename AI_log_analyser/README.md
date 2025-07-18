# AI Log Analyser

A comprehensive collection of log analysis tools combining traditional rule-based approaches with AI-powered anomaly detection for system monitoring and operations intelligence.

## Repository Structure

```
AI_log_analyser/
├── ai_log_analyser/           # AI-powered log analysis tools
│   ├── ai_log_analyser.py     # Main AI-based analyzer
│   ├── requirements.txt       # Python dependencies
│   └── README.md             # Detailed documentation
├── simple_log_analyser/       # Rule-based log analysis scripts
│   ├── 01_log_analyser.py     # Basic anomaly detection
│   ├── 02_log_analyser.py     # Enhanced with output options
│   ├── 03_log_analyser.py     # Simplified version
│   └── requirements.txt       # Python dependencies
└── README.md                 # This file
```

## Overview

This repository provides two complementary approaches to log analysis:

### AI-Powered Analysis (`ai_log_analyser/`)
Advanced log analysis using artificial intelligence and machine learning techniques for:
- Intelligent pattern recognition
- Automated anomaly detection
- Natural language processing of log messages
- Predictive analysis and trend detection

### Rule-Based Analysis (`simple_log_analyser/`)
Traditional threshold-based log analysis for:
- Quick anomaly detection
- Error frequency monitoring
- Time-window based analysis
- Lightweight system monitoring

## Quick Start

### Simple Log Analyser
For basic anomaly detection based on error frequency:

```bash
cd simple_log_analyser
pip install -r requirements.txt
python 02_log_analyser.py /path/to/your/logfile.log 1
```

### AI Log Analyser
For advanced AI-powered analysis:

```bash
cd ai_log_analyser
pip install -r requirements.txt
python ai_log_analyser.py --config config.json
```

## Features Comparison

| Feature | Simple Log Analyser | AI Log Analyser |
|---------|-------------------|-----------------|
| **Setup Complexity** | Low | Medium |
| **Processing Speed** | Fast | Moderate |
| **Accuracy** | Good for known patterns | Excellent for unknown patterns |
| **Resource Usage** | Low | Higher |
| **Customization** | Limited | Extensive |
| **Learning Capability** | None | Adaptive |
| **False Positives** | Higher | Lower |

## Use Cases

### Development & Testing
- **Simple Log Analyser**: Quick error detection during development
- **AI Log Analyser**: Comprehensive testing log analysis

### Production Monitoring
- **Simple Log Analyser**: Real-time alerting for known error patterns
- **AI Log Analyser**: Intelligent monitoring for unknown anomalies

### Incident Response
- **Simple Log Analyser**: Fast initial triage
- **AI Log Analyser**: Deep root cause analysis

### Capacity Planning
- **Simple Log Analyser**: Basic trend monitoring
- **AI Log Analyser**: Predictive analysis and forecasting

## Prerequisites

### System Requirements
- Python 3.7+
- Minimum 4GB RAM (8GB recommended for AI analyser)
- 1GB free disk space

### Common Dependencies
- pandas
- numpy
- python-dateutil

### AI-Specific Dependencies
- scikit-learn
- tensorflow (optional)
- transformers (optional)
- matplotlib (for visualization)

## Installation

### Option 1: Full Installation
```bash
git clone https://github.com/abcofdevops/aiops.git
cd aiops/AI_log_analyser

# Install all dependencies
pip install -r ai_log_analyser/requirements.txt
pip install -r simple_log_analyser/requirements.txt
```

### Option 2: Selective Installation
```bash
# For simple analysis only
cd simple_log_analyser
pip install -r requirements.txt

# For AI analysis only
cd ai_log_analyser
pip install -r requirements.txt
```

## Configuration

### Log Format Support
Both tools support standard log formats:
- Apache/Nginx access logs
- System logs (syslog format)
- Application logs with timestamps
- Custom structured formats

### Customization Options
- **Threshold Configuration**: Adjust sensitivity levels
- **Time Windows**: Configure analysis intervals
- **Output Formats**: Choose between concise and detailed reports
- **Alert Integration**: Connect with monitoring systems

## Examples

### Detecting Error Spikes
```bash
# Simple threshold-based detection
python simple_log_analyser/02_log_analyser.py server.log 1

# AI-powered anomaly detection
python ai_log_analyser/ai_log_analyser.py --input server.log --model adaptive
```

### Batch Analysis
```bash
# Analyze multiple log files
for log in *.log; do
    python simple_log_analyser/01_log_analyser.py "$log"
done
```

## Contributing

We welcome contributions! Here's how you can help:

1. **Bug Reports**: Submit issues with detailed descriptions
2. **Feature Requests**: Suggest new analysis capabilities
3. **Code Contributions**: 
   - Fork the repository
   - Create a feature branch
   - Submit a pull request

### Development Setup
```bash
git clone https://github.com/abcofdevops/aiops.git
cd aiops/AI_log_analyser

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
```

## Performance Considerations

### Simple Log Analyser
- **Processing Speed**: ~1M lines/minute
- **Memory Usage**: ~100MB for 1M lines
- **Best For**: Real-time monitoring, quick analysis

### AI Log Analyser
- **Processing Speed**: ~100K lines/minute
- **Memory Usage**: ~500MB-2GB depending on model
- **Best For**: Deep analysis, pattern discovery

## Troubleshooting

### Common Issues
1. **Memory Errors**: Reduce batch size or use streaming processing
2. **Slow Performance**: Check available system resources
3. **Parsing Errors**: Verify log format compatibility
4. **Missing Dependencies**: Install required packages

### Performance Optimization
- Use appropriate batch sizes
- Configure memory limits
- Enable parallel processing where available
- Consider log preprocessing for better performance

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

- **Documentation**: Check individual README files in each directory
- **Issues**: Report bugs and request features via GitHub Issues
- **Discussions**: Join the community discussions for questions and tips

## Related Projects

- **AIOps Tools**: Collection of AI-powered operations tools
- **Log Processing Pipeline**: End-to-end log processing solutions
- **Monitoring Integrations**: Plugins for popular monitoring systems

---

For detailed documentation on each component, refer to the README files in the respective directories:
- [AI Log Analyser Documentation](ai_log_analyser/README.md)
- [Simple Log Analyser Documentation](simple_log_analyser/README.md)
