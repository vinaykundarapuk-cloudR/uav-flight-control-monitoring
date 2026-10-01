# UAV Flight Control & System Monitoring

A Python-based UAV systems project that combines Linux system monitoring, automated telemetry collection, data analysis, and resource visualization.

## Project Overview

This project simulates a UAV support-monitoring workflow by collecting system resource metrics and analyzing them over time.

The system collects:

- CPU utilization
- Memory utilization
- Disk utilization
- Timestamped telemetry data

The collected metrics are stored as CSV data and analyzed using Python and Pandas. Monitoring results are also visualized using Matplotlib.

## Technologies

- Python
- Pandas
- NumPy
- Linux/Unix
- Matplotlib
- psutil
- CSV
- Git

## Project Structure

```text
uav-flight-control-monitoring/
├── data/
│   └── system_metrics.csv
├── dashboard/
│   └── system_metrics.png
├── docs/
├── scripts/
│   ├── analyze_metrics.py
│   └── visualize_metrics.py
├── src/
│   ├── flight_logger.py
│   └── system_monitor.py
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
