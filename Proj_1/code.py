import psutil
import time
import datetime
import subprocess

TARGET = "8.8.8.8"  # Google DNS 

downtime_events = 0
total_checks = 0
downtime_seconds = 0

log_file = "uptime_log.txt"


def get_system_uptime():
    boot_time = psutil.boot_time()
    return time.time() - boot_time

def ping_host(host):
    try:
        output = subprocess.run(
            ["ping", "-n", "1", host],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return output.returncode == 0
    except:
        return False


def log(msg):
    print(msg)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


print("🚀 Starting Monitoring (No SNMP)...\n")

while True:
    total_checks += 1
    current_time = datetime.datetime.now()

    uptime = get_system_uptime()
    is_up = ping_host(TARGET)

    if not is_up:
        log(f"[{current_time}] ❌ Target DOWN")
        downtime_events += 1
        downtime_seconds += 10
    else:
        log(f"[{current_time}] ✅ Target UP | Uptime: {uptime:.2f} sec")

    # SLA Calculation
    sla = ((total_checks - downtime_events) / total_checks) * 100

    log(f"SLA: {sla:.2f}%\n")

    time.sleep(10)