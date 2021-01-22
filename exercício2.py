#!/usr/bin/python3

print ("\n Expressão FOR") 
x = ["windows", "macos", "linux", "solaris", "ios"]
for item in x:
    if item != "solaris":
        print(item)


print ("\n Expressão WHILE")
b = 0
while b < len (x):
    if x[b] !="solaris":
        print(x[b])
    b += 1 
