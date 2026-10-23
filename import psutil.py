import psutil
import time
import requests

# Configuration
CPU_THRESHOLD = 80.0  # Percentage
WEBHOOK_URL = "YOUR_DISCORD_OR_SLACK_WEBHOOK_URL_HERE"

def check_system_health():
    # Get current CPU and RAM usage
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    
    print(f"Checking system stats... CPU: {cpu_usage}% | RAM: {ram_usage}%")
    
    # Check if CPU usage exceeds the safe limit
    if cpu_usage > CPU_THRESHOLD:
        alert_message = f"🚨 WARNING: High CPU usage detected! Current Load: {cpu_usage}%"
        print(alert_message)
        send_alert(alert_message)

def send_alert(message):
    # This simulates a DevOps monitoring alert sent to an operations channel
    payload = {"content": message} # Use {"text": message} if you are using Slack
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 204 or response.status_code == 200:
            print("Alert successfully sent to DevOps chat channel!")
    except Exception as e:
        print(f"Failed to send alert: {e}")

# Run the monitor loop every 5 seconds
if __name__ == "__main__":
    print("DevOps Monitoring Agent Started...")
    while True:
        check_system_health()
        time.sleep(5)
