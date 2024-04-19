import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
data_size = ["128", "256", "512", "1024", "1280"]
throughput_80 = [100, 120, 150, 180, 200]  # Throughput at 80% utilization
std_dev_80 = [5, 8, 10, 12, 15]  # Standard deviation at 80% utilization
throughput_100 = [120, 140, 160, 200, 220]  # Throughput at 100% utilization
std_dev_100 = [7, 10, 12, 15, 18]  # Standard deviation at 100% utilization

media100 = [20.620733361159985, 40.815783201715234, 81.62645765154348, 93.07873470333224, 94.39138071112653]
media80 = [20.419742163220544, 41.12581551167592, 79.63878960532773, 80.02467076617415, 80.14419824489894]
sd100 = [1.1968220451302027, 3.3446085319370167, 5.717115156415788, 5.181732589035829, 2.09857483664139]
sd80 = [1.7242327881292658, 2.68098131294511, 6.13530192713981, 1.3790439982840272, 1.5986540742909552]
# Calculate means
mean_80 = sum(throughput_80) / len(throughput_80)
mean_100 = sum(throughput_100) / len(throughput_100)

# Create the plot
plt.figure(figsize=(12, 6))

teorico100 = [100, 100, 100, 100, 100]

# Plot data points with error bars
plt.errorbar(data_size, media80, yerr=sd80, fmt='o-', label='80% de Banda ')
plt.errorbar(data_size, media100, yerr=sd100, fmt='s-', label='100% de Banda')
plt.errorbar(data_size, teorico100, yerr=0, fmt='s-', label='Teórico')

# Plot mean lines

# Set labels and title
plt.xlabel('Tamanho do Datagrama UDP (Bytes)')
plt.ylabel('Throughput Bytes por segundo')
plt.title('Resultados do Cenário A')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
#plt.tight_layout()
plt.show()

