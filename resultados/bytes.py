import json
import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with your actual data)
data_size = ["128", "256", "512", "1024", "1280"]


#Cenario A
mediaA100 = [65.93458951731374, 79.41841187548211, 88.51384727805123, 93.90760370946754, 95.05290233723846]
mediaA80 = [65.97162686891608, 79.50681382959549, 80.39429924284659, 80.32912797609114, 80.08989300725533]
stdA100 = [0.9357542151517976, 0.5764023336483733, 0.47830320883104044, 0.4725569672211932, 0.7843674841380243]
stdA80 = [0.34272484137262177, 0.41463837137117576, 2.734207735273849, 2.459441637537819, 2.3870869220449356]



#Cenario B
mediaB100 = [65.94302901298484, 79.48894346114186, 88.53610277417398, 93.6121773547816, 95.06054355132446]
mediaB80 = [65.84102540362571, 79.5525296222884, 80.68561626453425, 79.48572767641082, 80.0743201480635]
stdB100 = [0.5589800732970427, 0.6317522822402175, 0.35274886999333366, 5.411348238562207, 0.23288050627884924]
stdB80 = [1.1412806902391894, 0.7373004001946577, 3.972093799787951, 6.764921825331455, 1.4706139985466078]


#Cenario C
mediaC100 = [65.93134166877643, 79.47436020700367, 88.5494403541392, 93.91055033587169, 93.46228930737605]
mediaC80 = [65.98695775210464, 79.47504015960179, 79.89670106203152, 80.28498713918042, 80.2121411808586]
stdC100 = [1.0533388512872923, 0.5226214729693914, 0.5844168689206417, 0.7742271006562341, 4.718324248892993]
stdC80 = [0.8128719908925778, 0.8178329722177792, 2.0603518371664196, 1.9395302092725875, 1.789702486993742]

#Cenario D
mediaD100 = [20.99157823520477, 36.93574538793821, 54.24249189015907, 38.3942418815593, 44.271885548434696]
mediaD80 = [20.7546837825918, 39.19020011027558, 56.9819651279579, 47.370065162066304, 79.15590899527285]
stdD100 = [6.984072911576058, 15.591764480170918, 24.441542204360246, 38.73877012861337, 42.59436258965563]
stdD80 = [7.203842082287303, 15.649233571002862, 21.81467263948479, 35.04269646117008, 5.323740710953202]






red = "#d73737"
blue = "#6684e1"
green = "#60ac39"
purple = "#b854d4"



fig, axs = plt.subplots(2, 2, figsize=(10, 10))
# Create the plot
#plt.figure(figsize=(12, 6))

teorico100 = [100, 100, 100, 100, 100]
teorico80 = [80, 80, 80, 80, 80]

# Plot data points with error bars
axs[0, 0].errorbar(data_size, mediaA80, yerr=stdA80, fmt='o-', color=red, label='80% de Banda ')
axs[0, 0].errorbar(data_size, mediaA100, yerr=stdA100, fmt='s-',color=blue, label='100% de Banda')
axs[0, 0].errorbar(data_size, teorico80, yerr=0, fmt=':',color=green, label='Teórico 80% Banda')
axs[0, 0].errorbar(data_size, teorico100, yerr=0, fmt=':',color=purple, label='Teórico 100% Banda')

axs[1, 0].errorbar(data_size, mediaB80, yerr=stdB80, fmt='o-',color=red, label='80% de Banda ')
axs[1, 0].errorbar(data_size, mediaB100, yerr=stdB100, fmt='s-',color=blue, label='100% de Banda')
axs[1, 0].errorbar(data_size, teorico80, yerr=0, fmt=':',color=green, label='Teórico 80% Banda')
axs[1, 0].errorbar(data_size, teorico100, yerr=0, fmt=':',color=purple, label='Teórico 100% Banda')

axs[0, 1].errorbar(data_size, mediaC80, yerr=stdC80, fmt='o-',color=red, label='80% de Banda ')
axs[0, 1].errorbar(data_size, mediaC100, yerr=stdC100, fmt='s-',color=blue, label='100% de Banda')
axs[0, 1].errorbar(data_size, teorico80, yerr=0, fmt=':',color=green, label='Teórico 80% Banda')
axs[0, 1].errorbar(data_size, teorico100, yerr=0, fmt=':',color=purple, label='Teórico 100% Banda')

axs[1, 1].errorbar(data_size, mediaD80, yerr=stdD80, fmt='o-',color=red, label='80% de Banda ')
axs[1, 1].errorbar(data_size, mediaD100, yerr=stdD100, fmt='s-',color=blue, label='100% de Banda')
axs[1, 1].errorbar(data_size, teorico80, yerr=0, fmt=':',color=green, label='Teórico 80% Banda')
axs[1, 1].errorbar(data_size, teorico100, yerr=0, fmt=':',color=purple, label='Teórico 100% Banda')



#axs.ylabel('Throughput (Bytes por Segundo)')
axs[0, 0].set_title('Cenário I')
axs[1, 0].set_title('Cenário II')
axs[0, 1].set_title('Cenário III')
axs[1, 1].set_title('Cenário IV')
# Plot mean lines
for ax in axs.flat:
    ax.set(xlabel='Tamanho do Datagrama UDP (Bytes)', ylabel='Throughput (Bytes por Segundo)')


# Set labels and title
#plt.xlabel('Tamanho do Datagrama UDP (Bytes)')
#plt.ylabel('Throughput Bytes por segundo')
#plt.title('Resultados do Cenário A')

# Add legend
plt.legend()

# Show the plot
plt.grid(False)
plt.tight_layout()
plt.show()
