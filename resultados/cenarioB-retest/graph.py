import json
import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with your actual data)
data_size = ["128", "256", "512", "1024", "1280"]

files128_100 = [
         "x00",
         "x01",
         "x02",
         "x03",
         "x04",
         "x05",
         "x06",
         "x07",
         "x08",
         "x09",
         ]

files256_100 = [
         "x20",
         "x21",
         "x22",
         "x23",
         "x24",
         "x25",
         "x26",
         "x27",
         "x28",
         "x29",
         ]

files512_100 = [
         "x40",
         "x41",
         "x42",
         "x43",
         "x44",
         "x45",
         "x46",
         "x47",
         "x48",
         "x49",
         ]
files1024_100 = [
         "x60",
         "x61",
         "x62",
         "x63",
         "x64",
         "x65",
         "x66",
         "x67",
         "x68",
         "x69",
         ]
files1280_100 = [
         "x80",
         "x81",
         "x82",
         "x83",
         "x84",
         "x85",
         "x86",
         "x87",
         "x88",
         "x89",
         ]

files128_80 = [
         "x10",
         "x11",
         "x12",
         "x13",
         "x14",
         "x15",
         "x16",
         "x17",
         "x18",
         "x19",
         ]

files256_80 = [
         "x30",
         "x31",
         "x32",
         "x33",
         "x34",
         "x35",
         "x36",
         "x37",
         "x38",
         "x39",
         ]

files512_80 = [
         "x50",
         "x51",
         "x52",
         "x53",
         "x54",
         "x55",
         "x56",
         "x57",
         "x58",
         "x59",
         ]
files1024_80 = [
         "x70",
         "x71",
         "x72",
         "x73",
         "x74",
         "x75",
         "x76",
         "x77",
         "x78",
         "x79",
         ]
files1280_80 = [
         "x9000",
         "x9001",
         "x9002",
         "x9003",
         "x9004",
         "x9005",
         "x9006",
         "x9007",
         "x9008",
         "x9009",
         ]


def read_file(file):
    with open(file, "r") as file:
        json_data = json.load(file)
        return json_data

def conv(x):
    return float(x['sum']['bits_per_second'])/1_000_000

def get_packages(x):
    pkgs = float((x['sum']['packets']))/1_000_000
    time = float((x['sum']['seconds']))/1_000_000
    
    return pkgs / time


    return float((x['sum']['packets'])/(x(['sum']['seconds']/1_000_000)))

def from_iter(x):
    return np.fromiter(map(conv, x['intervals']), float)

def same_thing(x):
    return np.fromiter(map(get_packages, x['intervals']), float)

def list_mean(file):
    mean = []
    for i in file:
        json_data = read_file(i)
        for e in from_iter(json_data):
            mean.append(e)
    return np.mean(mean)

def list_sd(file):
    sd = []
    for i in file:
        json_data = read_file(i)
        for e in from_iter(json_data):
            sd.append(e)
    return np.std(sd)


print(type(list_mean(files128_100)))

sd100 = []
sd100.append(list_sd(files128_100))
sd100.append(list_sd(files256_100))
sd100.append(list_sd(files512_100))
sd100.append(list_sd(files1024_100))
sd100.append(list_sd(files1280_100))
media100 = []
media100.append(list_mean(files128_100))
media100.append(list_mean(files256_100))
media100.append(list_mean(files512_100))
media100.append(list_mean(files1024_100))
media100.append(list_mean(files1280_100))


sd80 = []
sd80.append(list_sd(files128_80))
sd80.append(list_sd(files256_80))
sd80.append(list_sd(files512_80))
sd80.append(list_sd(files1024_80))
sd80.append(list_sd(files1280_80))
media80 = []
media80.append(list_mean(files128_80))
media80.append(list_mean(files256_80))
media80.append(list_mean(files512_80))
media80.append(list_mean(files1024_80))
media80.append(list_mean(files1280_80))



Amedia100 = [20.620733361159985, 40.815783201715234, 81.62645765154348, 93.07873470333224, 94.39138071112653]
Amedia80 = [20.419742163220544, 41.12581551167592, 79.63878960532773, 80.02467076617415, 80.14419824489894]
Asd100 = [1.1968220451302027, 3.3446085319370167, 5.717115156415788, 5.181732589035829, 2.09857483664139]
Asd80 = [1.7242327881292658, 2.68098131294511, 6.13530192713981, 1.3790439982840272, 1.5986540742909552]


print(media80)
# Calculate means

fig, axs = plt.subplots(2, 2)
# Create the plot
#plt.figure(figsize=(12, 6))

teorico100 = [100, 100, 100, 100, 100]

# Plot data points with error bars
axs[1, 0].errorbar(data_size, media80, yerr=sd80, fmt='o-', label='80% de Banda ')
axs[1, 0].errorbar(data_size, media100, yerr=sd100, fmt='s-', label='100% de Banda')
axs[1, 0].errorbar(data_size, teorico100, yerr=0, fmt='s-', label='Teórico')

axs[0, 0].errorbar(data_size, Amedia80, yerr=sd80, fmt='o-', label='80% de Banda ')
axs[0, 0].errorbar(data_size, Amedia100, yerr=sd100, fmt='s-', label='100% de Banda')
axs[0, 0].errorbar(data_size, teorico100, yerr=0, fmt='s-', label='Teórico')

axs[0, 1].errorbar(data_size, media80, yerr=sd80, fmt='o-', label='80% de Banda ')
axs[0, 1].errorbar(data_size, media100, yerr=sd100, fmt='s-', label='100% de Banda')
axs[0, 1].errorbar(data_size, teorico100, yerr=0, fmt='s-', label='Teórico')

axs[1, 1].errorbar(data_size, Amedia80, yerr=sd80, fmt='o-', label='80% de Banda ')
axs[1, 1].errorbar(data_size, Amedia100, yerr=sd100, fmt='s-', label='100% de Banda')
axs[1, 1].errorbar(data_size, teorico100, yerr=0, fmt='s-', label='Teórico')

#axs.ylabel('Throughput (Bytes por Segundo)')
axs[1, 0].set_title('Cenário B')
axs[0, 0].set_title('Cenário A')
axs[0, 1].set_title('Cenário C')
axs[1, 1].set_title('Cenário D')
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
