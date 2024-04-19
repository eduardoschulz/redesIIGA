# Faz a média e o desvio padrão dos resultados do iperf3
import json 
import numpy as np

labels = [ 
          "80% de Banda"
          "100% de Banda"
          ]

files = [ 
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


def read_file(file):
    with open(file, "r") as file:
        json_data = json.load(file)
        return json_data

def conv(x):
    return float(x['sum']['bits_per_second'])/1_000_000

def get_packages(x):
    pkgs = float((x['sum']['packets']))
    time = float((x['sum']['seconds']))
    
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

with open("media.txt", "a") as myfile:
    myfile.write("média 256byte - 100% thr e pkts\n")
    myfile.write(str(np.mean(test_list)) + "\n")
    myfile.write(str(np.mean(new_list)) + "\n")
    myfile.write(str(np.std(test_list)) + "\n")
    myfile.write(str(np.std(new_list)) + "\n")
    
