import json
import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with your actual data)
data_size = ["128", "256", "512", "1024", "1280"]


#Cenario A
mediaA100 = [0.001033349715015112, 0.0023824819217081314, 0.0, 0.0, 0.0]
mediaA80 = [0.0010623421198611399, 0.0006002316364480692, 0.0, 0.0, 0.0]
stdA100 = [0.00542967157188499, 0.013971370321579904, 0.0, 0.0, 0.0]
stdA80 = [0.005515246589216741, 0.003314821217962238, 0.0, 0.0, 0.0]


#Cenario B
mediaB100 = [0.0018377184783724687, 0.0015695631500394934, 0.00046393501728489325, 0.0, 0.00042407791005153324]
mediaB80 = [0.0005006160767494104, 0.0017990656231095387, 0.0, 0.0, 0.0]
stdB100 = [0.01567707121461567, 0.010141375309405237, 0.00773534256986407, 0.0, 0.007070791788381412]
stdB80 = [0.005904748056650561, 0.017337941544204004, 0.0, 0.0, 0.0]



#Cenario C
mediaC100 = [0.001445767558292614, 0.002204163460394972, 0.0003975850835852237, 0.0, 0.0013882986700025329]
mediaC80 = [0.002694061733771847, 0.0008760005216695528, 0.0, 7.33871701613637e-05, 0.0]
stdC100 = [0.01532589952193023, 0.01841471960336835, 0.004933625737845618, 0.0, 0.010526634552767086]
stdC80 = [0.021353764912113358, 0.011321385626181308, 0.0, 0.001223608652680031, 0.0]


#Cenario D
mediaD100 = [67.37597228536053, 52.48674356920508, 37.69617657243749, 15.70146701527526, 9.970599485821507]
mediaD80 = [67.73363843962962, 50.118286253292844, 28.796589907629034, 8.794741993474203, 1.1904538856173492]



red = "#d73737"
blue = "#6684e1"



#data_size = ["128-80%","128-100%", "256-80%","256-100%", "512-80%","512-100%", "1024-80%","1024-100%", "1280-80%", "1280-100%"]

fig, axs = plt.subplots(1, 2, figsize=(12, 10))
# Create the plot

plt.title('Resultados do Cenário IV')
# Plot data points with error bars
axs[1].bar(data_size, mediaD100, color=blue)

axs[0].bar(data_size, mediaD80, color=red)


axs[1].set_title('100% Banda')
axs[0].set_title('80% Banda')
# Plot mean lines
for ax in axs.flat:
    ax.set(xlabel='Tamanho do Datagrama UDP (Bytes)', ylabel="Pacotes Perdidos (%)")


# Set labels and title
#plt.xlabel('Tamanho do Datagrama UDP (Bytes)')
#plt.ylabel('Throughput Bytes por segundo')

# Add legend
plt.legend()

# Show the plot
plt.grid(False)
plt.tight_layout()
plt.show()
