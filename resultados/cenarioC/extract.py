# Faz a média e o desvio padrão dos resultados do iperf3
import json 
import numpy as np

labels = [ 
          "80% de Banda"
          "100% de Banda"
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

if __name__ == "__main__":

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

    for i in range(10):
        if i == 0:
            files128100.append("res.json")
        else:
            files128100.append("res{}.json".format(i))

    print(files128100)

print(list_mean(files128100))
