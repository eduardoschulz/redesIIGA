import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
data_size = [128, 256, 512, 1024, 1280]
throughput_80 = [100, 120, 150, 180, 200]  # Throughput at 80% utilization
std_dev_80 = [5, 8, 10, 12, 15]  # Standard deviation at 80% utilization
throughput_100 = [120, 140, 160, 200, 220]  # Throughput at 100% utilization
std_dev_100 = [7, 10, 12, 15, 18]  # Standard deviation at 100% utilization
theoretical_throughput = 250  # Mb/s (example)

# Calculate means
mean_80 = sum(throughput_80) / len(throughput_80)
mean_100 = sum(throughput_100) / len(throughput_100)


# Define theoretical throughput (replace with your value)

# Plot theoretical throughput line


# Create the plot
plt.figure(figsize=(10, 6))

# Plot data points with error bars
plt.errorbar(data_size, throughput_80, yerr=std_dev_80, fmt='o-', label='80% Utilization')
plt.errorbar(data_size, throughput_100, yerr=std_dev_100, fmt='s-', label='100% Utilization')

# Plot mean lines
plt.axhline(y=mean_80, color='b', linestyle='--', label=f'Mean (80%) = {mean_80:.2f}')
plt.axhline(y=mean_100, color='r', linestyle='--', label=f'Mean (100%) = {mean_100:.2f}')
plt.axhline(y=theoretical_throughput, color='green', linestyle='-', label='Theoretical Throughput')

# Set labels and title
plt.xlabel('Data Size (Bytes)')
plt.ylabel('Throughput')
plt.title('Throughput Test Results')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()

