import csv
import os
import time
from datetime import datetime

from system_monitor import collect_system_metrics


OUTPUT_FILE = "data/system_metrics.csv"


def log_metrics(samples=30, interval=2):
    os.makedirs("data", exist_ok=True)

    file_exists = os.path.exists(OUTPUT_FILE)

    with open(OUTPUT_FILE, "a", newline="") as file:
        fieldnames = ["timestamp", "cpu_percent", "memory_percent", "disk_percent"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        for _ in range(samples):
            metrics = collect_system_metrics()
            writer.writerow(metrics)
            print(metrics)
            time.sleep(interval)


if __name__ == "__main__":
    print("Starting UAV system metrics logger...")
    log_metrics()
    print(f"Metrics saved to {OUTPUT_FILE}")
