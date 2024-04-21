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
        json_data = json.load(file)
        return json_data

def conv(x):
    return float(x['sum']['bits_per_second'])/1_000_000

def jitter(x):
    return float(x['sum']['jitter_ms'])

def lost_pkt(x):
    return float(x['sum']['lost_percent'])
def get_packages(x):
    pkgs = float((x['sum']['packets']))/1_000_000
    time = float((x['sum']['seconds']))/1_000_000
    #return pkgs / time
    return float((x['sum']['packets'])/(x(['sum']['seconds']/1_000_000)))

def from_iter(x):
    return np.fromiter(map(conv, x['intervals']), float)

def same_thing(x):
    return np.fromiter(map(get_packages, x['intervals']), float)

def lost_pkt_from(x):
    return np.fromiter(map(lost_pkt, x['intervals']), float)

def jitter_from(x):
    return np.fromiter(map(jitter, x['intervals']), float)



def create_dataset(files):

    listadearrays = []
    for i in files:
        for item in i:
            listadearrays.append(jitter_from(read_file(i)))

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


print(files128080)

newlist = []


print(from_iter(read_file("res3.json")))

list_dataset128_100 = []

for i in files128100:
    for item in i:
        list_dataset128_100.append((from_iter(read_file(i))))

dataset128_100 = []

for i in list_dataset128_100:
    for y in i:
        dataset128_100.append(y)


print("lista 128-100")
print(create_dataset(files128100)) 
print("lista 128-80")
print(create_dataset(files12880))

print("lista 128-80")
print(create_dataset(files256100))
print("lista 128-80")
print(create_dataset(files25680))
print("lista 128-80")
print(create_dataset(files512100))
print("lista 128-80")
print(create_dataset(files51280))
print("lista 128-80")
print(create_dataset(files1024100))
print("lista 128-80")
print(create_dataset(files102480))
print("lista 128-80")
print(create_dataset(files1280100))
print("lista 128-80")
print(create_dataset(files128080))
print("lista 128-80")


with open("jitterB", "a") as myfile:
    myfile.write(str(create_dataset(files128100))+'\n')
    myfile.write(str(create_dataset(files12880))+'\n')
    myfile.write(str(create_dataset(files256100))+'\n')
    myfile.write(str(create_dataset(files25680))+'\n')
    myfile.write(str(create_dataset(files512100))+'\n')
    myfile.write(str(create_dataset(files51280))+'\n')
    myfile.write(str(create_dataset(files1024100))+'\n')
    myfile.write(str(create_dataset(files102480))+'\n')
    myfile.write(str(create_dataset(files1280100))+'\n')
    myfile.write(str(create_dataset(files128080))+'\n')


