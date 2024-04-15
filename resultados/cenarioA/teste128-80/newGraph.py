# Faz a média e o desvio padrão dos resultados do iperf3
import json 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


labels = [ 
          "80% de Banda"
          "100% de Banda"
          ]

files = [ 
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

fig, ax = plt.subplots()

def read_file(file):
    with open(file, "r") as file:
        json_data = json.load(file)
        return json_data

def conv(x):
    return float(x['sum']['bits_per_second'])/1_000_000

def from_iter(x):
    return np.fromiter(map(conv, x['intervals']), float)

if __name__ == "__main__":
    
    todo_mean = [] 
    test_list = []
    for i in files:
        json_data = read_file(i)
        for e in from_iter(json_data):
            test_list.append(e)

    print(test_list)
    print(np.std(test_list))
    print(np.mean(test_list))

    colors = ["#7EA16B", "#C3D898"]

    ax.set_ylabel("Taxa de Transferência (Mbps)", fontsize=15)

    #b = ax.boxplot(test_list, "80% de Banda")
    

    testes = ['128 à 80%', '128 à 100%']
    counts = [np.mean(test_list), 100]
    
    ax.bar(testes, counts)

    ax.set_ylim((0,100))
    plt.show()

    



