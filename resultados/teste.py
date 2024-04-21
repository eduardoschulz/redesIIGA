import ast
import matplotlib.pyplot as plt

data_size = ["128", "256", "512", "1024", "1280"]
files = [
    "jitterA",
    "jitterB",
    "jitterC",
    "jitterD",
]

# Open the file and read its content
listaA, listaB, listaC, listaD = [], [], [], []
for filename in files:
    with open(filename) as f:
        content = f.readlines()
        for line in content:
            data = ast.literal_eval(line)
            if filename == "jitterA":
                listaA.append(data)
            elif filename == "jitterB":
                listaB.append(data)
            elif filename == "jitterC":
                listaC.append(data)
            else:
                listaD.append(data)

# Create the subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Create boxplots for each letter (file) on separate subplots
axs[0, 0].boxplot(listaA, labels=data_size)
axs[0, 1].boxplot(listaB, labels=data_size)
axs[1, 0].boxplot(listaC, labels=data_size)
axs[1, 1].boxplot(listaD, labels=data_size)

plt.tight_layout()  # Adjust spacing to prevent overlapping elements
plt.show()

