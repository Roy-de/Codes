import random

def empirical_distribution(data):
    n = len(data)
    cdf = []
    cumulative_frequency = 0
    for x in data:
        cumulative_frequency += 1
        cdf.append(cumulative_frequency/n)
    u = random.uniform(0, 1)
    i = 0
    while i < len(cdf) and cdf[i] < u:
        i += 1
    return data[i]

trace_data = [100, 200, 150, 300, 250, 200, 150, 100, 300, 250, 200, 150, 100, 300, 250, 200]

sample = empirical_distribution(trace_data)

print(sample)
