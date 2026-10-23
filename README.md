# Multi-Core DevOps Infrastructure Monitor & Slack Alerter 🚨

A production-inspired site reliability engineering (SRE) tool built with **Python** to monitor host resources at a granular level and automate instant alert dispatch via webhooks.

## 🛠️ Tech Stack & Practices
* **Core Language:** Python 3
* **System Utilities:** `psutil` (thread-level hardware performance instrumentation)
* **DevOps Methodologies:** System Observability, Continuous Monitoring, Infrastructure Automation, **Secrets Management via Environment Variables**.

## 🚀 Key Features
* **Granular Multi-Core Metrics:** Evaluates resource depletion independently across individual logical processor cores (`percpu=True`).
* **Intelligent Thresholding:** Pinpoints isolated thread locks (e.g., single-threaded infinite loops) even when average global CPU usage appears stable.
* **Automated Webhook Integration:** Formats and pipes instant, actionable alert notifications straight into enterprise Slack chat operations channels.
* **Secured Design:** Decouples structural code from sensitive API keys using environment configuration variables.

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR-REPO-NAME
   ```

2. **Install core operational dependencies:**
   ```bash
   pip install psutil requests
   ```

3. **Secure Environment Variables Configuration:**
   Inject your unique Slack webhook endpoint directly into your environment runtime rather than hardcoding it:
   ```bash
   # For Windows PowerShell:
   $env:SLACK_WEBHOOK_URL="https://slack.com"
   ```

4. **Launch the monitoring agent pipeline:**
   ```bash
   python monitor.py
   ```

## 📊 Sample Dashboard Log Output
```text
Advanced Core-Level DevOps Monitoring Agent Started...

--- CPU Core Breakdown ---
Core 0: 12.4%
Core 1: 98.2%
Core 2: 8.5%
Core 3: 14.1%
Overall RAM Usage: 54.7%
--------------------------
🚨 DevOps ALERT: High load detected on specific processing units! -> Core 1 (98.2%)
Alert successfully sent to DevOps chat channel!
```
