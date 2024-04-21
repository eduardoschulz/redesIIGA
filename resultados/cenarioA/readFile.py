import ast
filename = "jitterA"

# Open the file and read its content.
with open(filename) as f:
    content = f.readlines()

# Display the file's content line by line.
lista = ""
for line in content:
    print(line, end="")
    lista = line

print(lista)
lista = ast.literal_eval(lista)
print(lista[0])
