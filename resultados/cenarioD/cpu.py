import json 
import numpy as np

files128100 = []
files12880 = []
files256100 = []
files25680 = []
files512100 = []
files51280 = []
files1024100 = []
files102480 = []
files1280100 = []
files128080 = []


def read_file(file):
    with open(file, "r") as file:
        data = json.load(file)
        return data 

def conv(x):
    return (x['end']['cpu_utilization_percent']['host_total'])

def conv_remote(x):
    return (x['end']['cpu_utilization_percent']['remote_total'])


def create_dataset(files):
    listadearrays = []
    for i in files:
        for item in i:
            listadearrays.append((conv(read_file(i))))
    
    return listadearrays

    
def create_dataset_remote(files):
    listadearrays = []
    for i in files:
        for item in i:
            listadearrays.append((conv_remote(read_file(i))))
    
    return listadearrays




for i in range(10):
    if i == 0:
        files128100.append("res.json")
    else:
        files128100.append("res{}.json".format(i))

for i in range(11,20):
    files12880.append("res{}.json".format(i))

for i in range(21,30):
    files256100.append("res{}.json".format(i))

for i in range(31,40):
    files25680.append("res{}.json".format(i))

for i in range(41,50):
    files512100.append("res{}.json".format(i))

for i in range(51,60):
    files51280.append("res{}.json".format(i))

for i in range(61,70):
    files1024100.append("res{}.json".format(i))

for i in range(71,80):
    files102480.append("res{}.json".format(i))

for i in range(81,90):
    files1280100.append("res{}.json".format(i))

for i in range(91,100):
    files128080.append("res{}.json".format(i))





hostmean = []
hostmean.append(np.mean(create_dataset(files128100)))
hostmean.append(np.mean(create_dataset(files256100)))
hostmean.append(np.mean(create_dataset(files512100)))
hostmean.append(np.mean(create_dataset(files1024100)))
hostmean.append(np.mean(create_dataset(files1280100)))

print("hostmean 100")
print(hostmean)

hoststd = []
hoststd.append(np.std(create_dataset(files128100)))
hoststd.append(np.std(create_dataset(files256100)))
hoststd.append(np.std(create_dataset(files512100)))
hoststd.append(np.std(create_dataset(files1024100)))
hoststd.append(np.std(create_dataset(files1280100)))

print("hoststd 100")
print(hoststd)

hostmean = []
hostmean.append(np.mean(create_dataset(files12880)))
hostmean.append(np.mean(create_dataset(files25680)))
hostmean.append(np.mean(create_dataset(files51280)))
hostmean.append(np.mean(create_dataset(files102480)))
hostmean.append(np.mean(create_dataset(files128080)))

print("hostmean 80")
print(hostmean)

hoststd = []
hoststd.append(np.std(create_dataset(files12880)))
hoststd.append(np.std(create_dataset(files25680)))
hoststd.append(np.std(create_dataset(files51280)))
hoststd.append(np.std(create_dataset(files102480)))
hoststd.append(np.std(create_dataset(files128080)))

print("hoststd 100")
print(hoststd)

remotemean = []
remotemean.append(np.mean(create_dataset_remote(files128100)))
remotemean.append(np.mean(create_dataset_remote(files256100)))
remotemean.append(np.mean(create_dataset_remote(files512100)))
remotemean.append(np.mean(create_dataset_remote(files1024100)))
remotemean.append(np.mean(create_dataset_remote(files1280100)))

print("remotemean 100")
print(remotemean)

remotestd = []
remotestd.append(np.std(create_dataset_remote(files128100)))
remotestd.append(np.std(create_dataset_remote(files256100)))
remotestd.append(np.std(create_dataset_remote(files512100)))
remotestd.append(np.std(create_dataset_remote(files1024100)))
remotestd.append(np.std(create_dataset_remote(files1280100)))

print("remotestd 100")
print(remotestd)

remotemean = []
remotemean.append(np.mean(create_dataset_remote(files12880)))
remotemean.append(np.mean(create_dataset_remote(files25680)))
remotemean.append(np.mean(create_dataset_remote(files51280)))
remotemean.append(np.mean(create_dataset_remote(files102480)))
remotemean.append(np.mean(create_dataset_remote(files128080)))

print("remotemean 80")
print(remotemean)

remotestd = []
remotestd.append(np.std(create_dataset_remote(files12880)))
remotestd.append(np.std(create_dataset_remote(files25680)))
remotestd.append(np.std(create_dataset_remote(files51280)))
remotestd.append(np.std(create_dataset_remote(files102480)))
remotestd.append(np.std(create_dataset_remote(files128080)))

print("remotestd 80")
print(remotestd)
