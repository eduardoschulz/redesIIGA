import ast
import matplotlib.pyplot as plt


data_size = ["128", "256", "512", "1024", "1280"]
files = [
    "jitterA",
    "jitterB",
    "jitterC",
    "jitterD",
    ]
# Open the file and read its content.

listaA = []
listaB = []
listaC = []
listaD = []

counter = 0
for i in files:
    with open(i) as f:
        content = f.readlines()
        for line in content:
            if counter == 0: 
                listaA.append(ast.literal_eval(line))
            elif counter == 1:
                listaB.append(ast.literal_eval(line))
            elif counter == 2:
                listaC.append(ast.literal_eval(line))
            elif counter == 3:
                listaD.append(ast.literal_eval(line))
    counter += 1


fig, axs = plt.subplots(2, 2, figsize=(20,15))

#axs[0,0].boxplot([listaA[0], listaA[2], listaA[4], listaA[6], listaA[8]])

a = list([listaA[0], listaA[2], listaA[4], listaA[6], listaA[8]])
b = list([listaB[0], listaB[2], listaB[4], listaB[6], listaB[8]])
c = list([listaC[0], listaC[2], listaB[4], listaC[6], listaC[8]])
d = list([listaD[0], listaD[2], listaD[4], listaD[6], listaD[8]])






xticks = ['128-100%', '128-80%', '256-100%', '256-80%', '512-100%','512-80%', '1024-100%','1024-80%', '1280-100%', '1280-80%']

axs[0,0].set_xticklabels(xticks)
axs[1,0].set_xticklabels(xticks)
axs[0,1].set_xticklabels(xticks)
axs[1,1].set_xticklabels(xticks)

axs[0,0].boxplot(listaA)
axs[1,0].boxplot(listaB)
axs[0,1].boxplot(listaC)
axs[1,1].boxplot(listaD)


axs[0, 0].set_title('Cenário I')
axs[1, 0].set_title('Cenário II')
axs[0, 1].set_title('Cenário III')
axs[1, 1].set_title('Cenário IV')

for ax in axs.flat:
    ax.set(xlabel='Tamanho do Datagrama UDP (Bytes)', ylabel='Jitter (ms)')

plt.show()

