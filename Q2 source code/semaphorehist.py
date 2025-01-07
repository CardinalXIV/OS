import matplotlib.pyplot as plt
import numpy as np
latencies = []
try:
    with open('semtest.txt') as f:#this needs to change based on the file its reading
        for line in f:
            line = line.strip()
            if line:
                try:
                    latencies.append(int(line))
                except ValueError : 
                    print(f"Skipping invalid entry: {line}")
except FileNotFoundError:
    print("The file 'semtest.txt' was not found.")
    exit()

latencies=np.array(latencies)
print(latencies)

if len(latencies) == 0:
    print("no data found")
    exit()
min_latency = np.min(latencies)
avg_latency = np.mean(latencies)
max_latency = np.max(latencies)

labels = ['Min Latency', 'Avg Latency', 'Max Latency']
values = [min_latency, avg_latency, max_latency]
plt.figure(figsize=(10, 5))

plt.barh(labels, values, color=['blue', 'green', 'red'])
plt.xlabel('Latency (ns)')
plt.ylabel('Latency Type')

plt.title('Semaphore Wait Time Statistics')
plt.xlim(0, max(values) + 10)  

for i, value in enumerate(values):

    plt.text(value + 1, i, f'{value:.2f}', va='center', ha='left')

plt.show()
