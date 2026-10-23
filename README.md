# Local System Infrastructure Monitor 🚨

A practical **Systems Engineering and DevOps automation tool** written in **Python** that monitors local host machine hardware performance in real-time and routes anomaly notifications straight into a live enterprise **Slack** workspace logs.

## ⚙️ Core Architecture & Concept
* **Systems Engineering (Observability):** Hooks into the local OS kernel to continuously profile resource utilization across individual, isolated logical processor cores (`percpu=True`).
* **DevOps Engineering (Automation):** Replaces manual oversight with an active, programmatic alert framework that instantly formats error telemetry logs and pipes them securely to team communication channels.

## 🚀 Key Features
* **Thread-Level Instrumentation:** Independently measures core workloads to isolate single-threaded loops that hidden system averages hide.
* **Secured Design (Secrets Management):** Decouples structural source code from production access paths using localized system environment variable lookups.
* **Instant Incident Communications:** Formats lightweight, automated outbound JSON request payloads matching enterprise Slack messaging schemas.

## 📦 Installation & Configuration Setup

1. **Clone your repository destination:**
   ```bash
   git clone https://github.com
   cd YOUR-REPOSITORY-NAME
   ```

2. **Install host environment utility packages:**
   ```bash
   pip install psutil requests
   ```

3. **Configure your runtime environment variables:**
   Inject your unique Slack webhook endpoint directly into your shell environment before launching (keeps code clean and safe):
   ```powershell
   # Windows PowerShell
   $env:SLACK_WEBHOOK_URL="https://slack.com"
   ```

4. **Launch the core monitoring pipeline agent:**
   ```bash
   python "import psutil.py"
   ```

## 📊 Sample Output Logs
```text
Advanced Core-Level DevOps Monitoring Agent Started...

--- CPU Core Breakdown ---
Core 0: 6.3%
Core 1: 18.2%
Core 2: 94.7%
Core 3: 11.1%
Overall RAM Usage: 71.4%
--------------------------
🚨 DevOps ALERT: High load detected on specific processing units! -> Core 2 (94.7%)
Alert successfully sent to DevOps chat channel!
```
