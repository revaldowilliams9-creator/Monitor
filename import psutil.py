import psutil
import time
import requests

# 1. YOUR REAL SLACK ENDPOINT CONFIGURATION
CPU_THRESHOLD = 10.0  # Percentage baseline for any single core
import os

# Instead of hardcoding, look for a variable configured on the computer running it
WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")


def check_system_health():
    # Setting percpu=True returns a list of percentages for each individual core
    core_usages = psutil.cpu_percent(interval=1, percpu=True)
    ram_usage = psutil.virtual_memory().percent
    
    # Print out the stats for each individual core cleanly in terminal
    print("\n--- CPU Core Breakdown ---")
    for core_index, core_percentage in enumerate(core_usages):
        print(f"Core {core_index}: {core_percentage}%")
    print(f"Overall RAM Usage: {ram_usage}%")
    print("--------------------------")
    
    # DevOps Automation: Check if ANY individual core is hitting the threshold limit
    high_load_cores = []
    for core_index, core_percentage in enumerate(core_usages):
        if core_percentage > CPU_THRESHOLD:
            high_load_cores.append(f"Core {core_index} ({core_percentage}%)")
            
    if high_load_cores:
        cores_alert_string = ", ".join(high_load_cores)
        alert_message = f"🚨 DevOps ALERT: High load detected on specific processing units! -> {cores_alert_string}"
        print(alert_message)
        send_alert(alert_message)

def send_alert(message):
    # CRITICAL SLACK FIX: Slack requires the key to be named "text" (not "content")
    payload = {"text": message} 
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            print("Alert successfully sent to DevOps chat channel!")
        else:
            print(f"Slack returned an error code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

if __name__ == "__main__":
    print("Advanced Core-Level DevOps Monitoring Agent Started...")
    while True:
        check_system_health()
        time.sleep(4) # Short sleep interval since cpu_percent already takes 1 second
