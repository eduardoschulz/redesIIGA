# Faz a média e o desvio padrão dos resultados do iperf3
import json 


labels = [ 
          "80% de Banda"
          "100% de Banda"
          ]

def read_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def extract(json):
    return json['sum']['bits_per_second']



if __name__ == "__main__":

    data = read_file("x00.json")

    time_intervals = data['intervals']
    time_intervals_sum = [item['sum'] for item in time_intervals]

    bits_per_second = [item['bits_per_second'] / 1000000 for item in time_intervals_sum]
    mean = 0
    for bps in bits_per_second:
        mean += bps
    
    mean = mean / len(bits_per_second)
    print(bits_per_second)
    print(mean)
