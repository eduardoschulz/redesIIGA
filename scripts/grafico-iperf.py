# Faz a média e o desvio padrão dos resultados do iperf3
import json 
import numpy as np

labels = [ 
          "80% de Banda"
          "100% de Banda"
          ]

files = [ 
         "x00.json",
         "x01.json",
         "x02.json",
         "x03.json",
         "x04.json",
         "x05.json",
         "x06.json",
         "x07.json",
         "x08.json",
         "x09.json",
         ]         

def read_file(filename):
    with open(filename, "r") as file:
        print(type(json))
        data = json.load(file)
    return data

def extract(json):
    return json['sum']['bits_per_second']

def getMean(data):

    time_intervals = data['intervals']
    time_intervals_sum = [item['sum'] for item in time_intervals]

    bits_per_second = [item['bits_per_second'] / 1000000 for item in time_intervals_sum]

    return np.mean(bits_per_second)


if __name__ == "__main__":
    
    for i in files:
        json = read_file(i)
        print(getMean(json))
