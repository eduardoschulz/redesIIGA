import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
data_size = [128, 256, 512, 1024, 1280]
throughput_80 = [100, 120, 150, 180, 200]
throughput_100 = [120, 140, 160, 200, 220]

# Create the boxplot
plt.figure(figsize=(10, 6))
bp = plt.boxplot([throughput_80, throughput_100])

# Customize box appearance

# Customize median line appearance

# Set labels and title
plt.xlabel('Throughput')
plt.ylabel('Data Size (Bytes)')
plt.title('Distribution of Throughput by Data Size and Utilization')

# Show the plot
#jplt.grid(True)
#plt.tight_layout()
plt.show()

