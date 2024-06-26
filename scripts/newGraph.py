# Faz a média e o desvio padrão dos resultados do iperf3
import json 
import numpy as np

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


def read_file(file):
    with open(file, "r") as file:
        json_data = json.load(file)
        return json_data

def conv(x):
    return float(x['sum']['bits_per_second'])/1_000_000

def from_iter(x):
    return np.fromiter(map(conv, x['intervals']), float)

if __name__ == "__main__":
    
    for i in files:
        json_data = read_file(i)
        print(from_iter(json_data))

