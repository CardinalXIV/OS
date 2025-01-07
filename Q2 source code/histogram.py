import matplotlib.pyplot as plt
import numpy as np
latencies = []
with open('cyclictest.txt') as f: #This needs to change based on the data file its reading
    for line in f:
        if line.startswith('#') or line.strip() == '':
            continue
        values = line.split()
        latencies.append(int(values[2])) #third column is latency thats why [2]
latencies = np.array(latencies)

mean_latency = np.mean(latencies)
std_latency = np.std(latencies)

print(f"Mean Latency: {mean_latency} µs")
print(f"Standard Deviation (Jitter): {std_latency} µs")

#to plot graph use this
plt.figure(figsize=(10, 5))
plt.hist(latencies, bins=600, color='red', edgecolor='red', log=True)
plt.xlabel('Latency (µs)')
plt.ylabel('Frequency Count')
plt.title('PREEMPT_RT Kernel Latency Histogram')
plt.show()
