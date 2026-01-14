import psutil
import datetime
import os

# The Manager's Secret (Loaded from the Cloud environment)
secret_key = os.getenv("MONITOR_PASSWORD")

def check_health():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"{timestamp} - CPU: {cpu}% - RAM: {ram}%"
    
    # Logic: If system is stressed, we mention the secret key (for testing)
    if cpu > 80 or ram > 80:
        print(f"ALERT! System Stressed. Security Token: {secret_key}")
    else:
        print(f"System Healthy. Log: {log_entry}")

    with open("system-log.txt", "a") as f:
        f.write(log_entry + "\n")

if __name__ == "__main__":
    check_health()