#!/usr/bin/python3

#ABRIR FICHEIRO
file = open("Exercício2_resultados.txt","w")

#CICLO FOR
file.write("\n CICLO FOR \n")
print("\n CICLO FOR \n")

x = ["windows", "macos", "linux", "solaris", "ios"]
for item in x:
    if item != "solaris":
        print(item)
        file.write(str(item) + "\n")

#CICLO WHILE
file.write ("\n CICLO WHILE \n")
print("\n CICLO WHILE \n")
b = 0
while b < len (x):
    if x[b] !="solaris":
        print(x[b])
        file.write(str(x[b])+ "\n")
    b += 1 

#FECHAR FICHEIRO
file.close()



