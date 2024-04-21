import numpy as np
import statistics

f = open("extract.txt", "r")
lines = f.readlines()

counter = 1

throughput_media = []
pkts_media = []
throughput_sd = []
pkts_sd = []

for line in lines:
    line = line.replace("\n", "")
    #print(line)
    lista = list(line)
    if counter == 1:
        print(statistics.fmean(lista))
        throughput_media.append(np.mean(lista))
        print(np.std(lista))
        throughput_sd.append(np.std(lista))
    elif counter != 1:
        print(np.mean(lista))
        pkts_media.append(np.mean(lista))
        print(np.std(lista))
        pkts_sd.append(np.std(lista))
        counter = 1

print(throughput_media)


