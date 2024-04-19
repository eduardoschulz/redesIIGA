# Faz a média e o desvio padrão dos resultados do iperf3
import json 
import numpy as np

labels = [ 
          "80% de Banda"
          "100% de Banda"
          ]

files = [ 
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

if __name__ == "__main__":
    
    todo_mean = [] 
    test_list = []
    new_list = []
    for i in files:
        json_data = read_file(i)
        for e in from_iter(json_data):
            test_list.append(e)

    for i in files:
        json_data = read_file(i)
        for e in same_thing(json_data):
            new_list.append(e)


    print(test_list)
    print(np.std(test_list))
    print(np.mean(test_list))

    print("Pkts: ")
    print(new_list)

with open("extract.txt", "a") as myfile:
    myfile.write("\n\n")
    myfile.write(str(test_list))
    myfile.write("\n\n")
    myfile.write(str(new_list))
    
