import pandas as pd

FILE = "data/system_metrics.csv"

df = pd.read_csv(FILE)

print("UAV System Metrics Analysis")
print("===========================")

print(f"\nSamples Collected: {len(df)}")

print("\nAverage Metrics:")
print(f"CPU Usage: {df['cpu_percent'].mean():.2f}%")
print(f"Memory Usage: {df['memory_percent'].mean():.2f}%")
print(f"Disk Usage: {df['disk_percent'].mean():.2f}%")

print("\nPeak Metrics:")
print(f"Peak CPU: {df['cpu_percent'].max():.2f}%")
print(f"Peak Memory: {df['memory_percent'].max():.2f}%")
print(f"Peak Disk: {df['disk_percent'].max():.2f}%")

print("\nSystem Status:")

if df["cpu_percent"].max() > 80:
    print("WARNING: High CPU utilization detected.")
else:
    print("CPU utilization remained within normal range.")

if df["memory_percent"].max() > 80:
    print("WARNING: High memory utilization detected.")
else:
    print("Memory utilization remained within normal range.")

if df["disk_percent"].max() > 80:
    print("WARNING: High disk utilization detected.")
else:
    print("Disk utilization remained within normal range.")
