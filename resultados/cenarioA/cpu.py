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


    listacompleta = []
    for i in listadearrays:
        for y in i:
            listacompleta.append(y)

    return listacompleta





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



    print(read_file("res.json"))


