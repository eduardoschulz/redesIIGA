import json
import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with your actual data)
data_size = ["128", "256", "512", "1024", "1280"]


#Cenario A
mediaA100 = [64392.70945148274, 38779.55366847921, 21610.589326978697, 11463.402215098948, 9282.556588290136]
mediaA80 = [64427.09135396098, 38823.02137679144, 19627.557473768557, 9805.887775327581, 7821.346714875275]
stdA100 = [920.5132943216985, 281.51885135295754, 117.60400890021927, 57.68805326358127, 76.59984278361111]

stdA80 = [335.02474244654206, 207.41181809230943, 667.5250184890053, 300.21319071599777, 233.11138501379506]




#Cenario B
mediaB100 = [64404.15822093056, 38814.88979045144, 21616.097044822065, 11427.773354366924, 9283.356564023385]
mediaB80 = [64300.041128853765, 38845.839453242734, 19698.704882233345, 9704.944989326814, 7819.8044213609855]
stdB100 = [572.3720250586896, 301.0627037657051, 82.66445726872205, 660.6575097987541, 22.763646446950933]
stdB80 = [1119.787445132991, 364.8062565556929, 969.737756950268, 826.0862721422357, 143.61215457855008]



#Cenario C
mediaC100 = [64387.2063372712, 38806.77542405762, 21618.69492209173, 11463.754742522093, 9127.345151355841]
mediaC80 = [64444.65899666555, 38811.576711669455, 19510.712034362517, 9805.214482004545, 7833.289492514927]
stdC100 = [1028.7408156117444, 255.2813071945075, 142.68833200998668, 94.5126661771467, 460.83304140020766]
stdC80 = [778.7737671123456, 353.99024636670026, 469.66202255647414, 261.0621815336913, 174.76665442859462]


#Cenario D
mediaD100 = [62950.11293665408, 41080.5934538708, 23345.810096663452, 11216.794784428717, 9094.903716540852]
mediaD80 = [62466.61665181681, 38361.48265599765, 19630.37895165735, 9695.916240870469, 7824.812906744061]

stdD100 = [8878.946088488432, 9035.069785837573, 5529.553457603263, 40355.70333869276, 32767.548328891226]

stdD80 = [9847.511518721783, 4350.805467236936, 1715.8121719213996, 29951.586780065398, 367.4239194748475]
 



red = "#d73737"
blue = "#6684e1"
green = "#60ac39"
purple = "#b854d4"



fig, axs = plt.subplots(2, 2, figsize=(10, 10))
# Create the plot
#plt.figure(figsize=(12, 6))

teorico80 = [80000000 / (128* 8),80000000 / (256* 8),80000000 / (512* 8),80000000 / (1024* 8), 80000000 / (1280* 8)]
teorico100 = [100000000 / (128* 8),100000000 / (256* 8),100000000 / (512* 8),100000000 / (1024* 8), 100000000 / (1280* 8)]
teoricoth = (teorico80[4] * 128 *8)
print(teoricoth)

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
axs[1, 0].set_title('Cenário II')
axs[0, 0].set_title('Cenário I')
axs[0, 1].set_title('Cenário III')
axs[1, 1].set_title('Cenário IV')
# Plot mean lines
for ax in axs.flat:
    ax.set(xlabel='Tamanho do Datagrama UDP (Bytes)', ylabel='Número de Pacotes enviadospor segundo')


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
