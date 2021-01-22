#!/usr/bin/python3

ipLista = []
portLista = []

File1= open("ipList.txt", "w")
File2 = open("portList.txt", "w")

for ip in range(1, 256):
    print(ip)
    File1.write(str(ip) + "\n")

for port in range(1, 1025):
    print(port)
    File2.write(str(port) + "\n")

File1.close()
File2.close()
