import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/system_metrics.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["cpu_percent"], label="CPU Usage")
plt.plot(df["timestamp"], df["memory_percent"], label="Memory Usage")

plt.title("UAV System Resource Monitoring")
plt.xlabel("Time")
plt.ylabel("Usage (%)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("dashboard/system_metrics.png", dpi=150)
plt.show()
