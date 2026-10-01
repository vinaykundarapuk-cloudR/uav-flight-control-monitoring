import psutil
import time
from datetime import datetime


def collect_system_metrics():
    return {
        "timestamp": datetime.now().isoformat(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage("/").percent,
    }


if __name__ == "__main__":
    print("UAV System Monitoring")
    print("=====================")

    for _ in range(5):
        metrics = collect_system_metrics()
        print(metrics)
        time.sleep(1)
