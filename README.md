# DevOps Infrastructure Monitor 🚨

A lightweight infrastructure health monitoring script written in **Python** that simulates real-world DevOps site reliability engineering (SRE) operations. It tracks real-time host resource depletion and alerts engineering teams instantly through chat integrations.

## 🛠️ Tech Stack & Concepts
* **Language:** Python 3
* **Libraries:** `psutil` (system performance collection), `requests` (HTTP payload transmission)
* **DevOps Practice:** System Observability, Continuous Monitoring, Infrastructure Alerting automation.

## 🚀 Features
* Continuously checks local machine CPU and RAM utilization metrics at custom intervals.
* Compares usage anomalies against a configurable threshold safety baseline (e.g., 80%).
* Automates outbound alert notifications via webhook POST payloads directly into engineering communication channels (Slack/Discord).

## 📦 Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR-REPO-NAME
   ```

2. **Install core operational dependencies:**
   ```bash
   pip install psutil requests
   ```

3. **Configure your environmental endpoint:**
   Open `monitor.py` and assign your active communications endpoint to the configuration block:
   ```python
   WEBHOOK_URL = "YOUR_COPIED_WEBHOOK_ENDPOINT_HERE"
   ```

4. **Launch the monitoring agent pipeline:**
   ```bash
   python monitor.py
   ```

## 📊 Sample Output
```text
DevOps Monitoring Agent Started...
Checking system stats... CPU: 12.4% | RAM: 58.1%
Checking system stats... CPU: 18.9% | RAM: 58.2%
🚨 WARNING: High CPU usage detected! Current Load: 86.4%
Alert successfully sent to DevOps chat channel!
```
