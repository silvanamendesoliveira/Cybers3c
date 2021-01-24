#!/usr/bin/python3

import os, datetime, socket, time, threading

# pedir o input ao utilizador
ip = input("Por favor insira um IP válido: ")

# criar diretório Scans
if not os.path.isdir("Scans"):
    os.mkdir("Scans") 
    os.chdir("Scans") 

def portScanner(ip, port):
    with thread_lock:
        try:
            file = open("portscan.txt", "a")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port)) 
            if result == 0:
                print("Port " + str(port) + " is open \n")
                file.write("Port" + str(port) + " is open \n")
            else:
                print("Port " + str(port) + " is closed \n")
            sock.close()
            file.close()
   
        except socket.gaierror:
            print("Não foi possível identificar o endereço.")
        except socket.error:
            print("Ocorreu um erro de socket.")
        except KeyboardInterrupt:
            print("Scan terminado com sucesso.")
        except:
            print("Ocorreu um erro.")

#EXERCÍCIO 2 - THREADS

t0 = datetime.datetime.now()
if __name__ == "__main__":
    thread_lock = threading.Lock()
    port =0
    for port in range (1, 1025):
        thread = threading.Thread(target=portScanner, args=(ip,port))
        thread.start()
    thread.join()


t1 = datetime.datetime.now() - t0
print("Demorou" + str(t1) + "segundos")
  


    