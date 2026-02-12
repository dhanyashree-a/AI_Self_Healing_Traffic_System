import pandas as pd
import matplotlib.pyplot as plt

# Read CSV files
#ai_data = pd.read_csv("evaluation/ai_metrics.csv")
#fixed_data = pd.read_csv("evaluation/fixed_metrics.csv")
ai_data = pd.read_csv("evaluation/ai_metrics.csv")
fixed_data = pd.read_csv("evaluation/fixed_metrics.csv")



# ========================
# Calculate Final Metrics
# ========================

ai_avg_wait = ai_data["AvgWaitingTime"].mean()
fixed_avg_wait = fixed_data["AvgWaitingTime"].mean()

ai_avg_queue = ai_data["QueueLength"].mean()
fixed_avg_queue = fixed_data["QueueLength"].mean()

# ========================
# PLOT 1: Waiting Time Trend
# ========================

plt.figure()
plt.plot(ai_data["Step"], ai_data["AvgWaitingTime"], label="AI")
plt.plot(fixed_data["Step"], fixed_data["AvgWaitingTime"], label="Fixed")
plt.xlabel("Simulation Step")
plt.ylabel("Average Waiting Time")
plt.title("Waiting Time Trend Comparison")
plt.legend()
plt.grid(True)
plt.show()

# ========================
# PLOT 2: Queue Length Trend
# ========================

plt.figure()
plt.plot(ai_data["Step"], ai_data["QueueLength"], label="AI")
plt.plot(fixed_data["Step"], fixed_data["QueueLength"], label="Fixed")
plt.xlabel("Simulation Step")
plt.ylabel("Queue Length")
plt.title("Queue Length Comparison")
plt.legend()
plt.grid(True)
plt.show()

# ========================
# PLOT 3: Final Metric Comparison
# ========================

metrics = ["Waiting Time", "Queue Length"]
ai_values = [ai_avg_wait, ai_avg_queue]
fixed_values = [fixed_avg_wait, fixed_avg_queue]

x = range(len(metrics))

plt.figure()
plt.plot(x, fixed_values, marker='o', label="Fixed-Time")
plt.plot(x, ai_values, marker='o', label="AI-Based")
plt.xticks(x, metrics)
plt.ylabel("Performance Value")
plt.title("Final Performance Comparison")
plt.legend()
plt.grid(True)
plt.show()

print("\n===== FINAL COMPARISON =====")
print(f"AI Avg Waiting Time: {ai_avg_wait:.2f}")
print(f"Fixed Avg Waiting Time: {fixed_avg_wait:.2f}")
print(f"AI Avg Queue Length: {ai_avg_queue:.2f}")
print(f"Fixed Avg Queue Length: {fixed_avg_queue:.2f}")
print("============================")
