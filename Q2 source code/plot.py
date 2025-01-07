import matplotlib.pyplot as plt
import numpy as np

def parse_cyclictest_results(file_path):
    latencies = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#') or line.strip() == '':
                continue
            values = line.split()
            if len(values) > 2:  # Ensure there are enough columns
                try:
                    latencies.append(int(values[2]))  # Assuming the third column is the latency
                except ValueError:
                    continue  # Skip lines where conversion to int fails
    return np.array(latencies)

def plot_latency_histogram(latencies, title):
    mean_latency = np.mean(latencies)
    std_latency = np.std(latencies)

    print(f"{title} - Mean Latency: {mean_latency} µs")
    print(f"{title} - Standard Deviation (Jitter): {std_latency} µs")

    plt.figure(figsize=(10, 5))
    plt.hist(latencies, bins=600, color='red', edgecolor='red', log=True)
    plt.xlabel('Latency (µs)')
    plt.ylabel('Frequency Count')
    plt.title(f'{title} - Latency Histogram')
    plt.show()

# Paths to your files
no_load_path = 'cyclictest_no_load_soft_results.txt'
medium_load_path = 'cyclictest_medium_load_soft_results.txt'
heavy_load_path = 'cyclictest_heavy_load_soft_results.txt'

# Parse the files
no_load_latencies = parse_cyclictest_results(no_load_path)
medium_load_latencies = parse_cyclictest_results(medium_load_path)
heavy_load_latencies = parse_cyclictest_results(heavy_load_path)

# Plot the results
plot_latency_histogram(no_load_latencies, 'No Load')
plot_latency_histogram(medium_load_latencies, 'Medium Load')
plot_latency_histogram(heavy_load_latencies, 'Heavy Load')
