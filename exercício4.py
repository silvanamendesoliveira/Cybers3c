#!/usr/bin/python3

import os, sys
path = "."




#Criar diretórios
def makeDir():
    print("Criar diretório")
    nome1 = input ("Introduza o nome para o diretório: ")
    if os.path.exists(nome1):
        print("ERRO: Este nome já existe. Atribua outro.")
    else:
        print("Diretório criado com sucesso!\n")
        os.mkdir(nome1)
        main()

#Renomear dirétórios
def renameDir():
    print("Renomear o diretório")
    new_n = input ("Introduza o nome do diretório que pretende renomear: ")
    if os.path.exists(path):
        novonome = input ("Introduza o novo nome:") 
        os.rename(new_n, novonome)
        print("O nome foi alterado com sucesso!")
        main()
    else:
        print("O nome indicado não existe.")
    
# Remover diretórios
def remDir():
    print ("Eliminar diretório")
    nome = input ("Introduza o nome do diretório que pretende eliminar: ")
    if os.path.exists(nome):
        os.rmdir(nome)
        print("Diretório eliminado com sucesso!")
        main()   
    else:
        print("O nome indicado não existe.")  
        main ()
 
#Listar diretórios
def listDir():
    print (os.listdir())
    main()

def main():
    print("\nOPÇÕES: \n[C] Criar um diretório \n[R] Remover um diretório \n[L] Listar aos diretórios existentes \n[N] Renomear um diretório\n[S] Sair\n")
    resposta = input("\nIntroduza a letra maiúscula da opção que pretende: ")
    if resposta == "C":
        makeDir()

    if resposta == "R":
        remDir()

    if resposta == "L":
        listDir()

    if resposta == "N":
        renameDir()

    if resposta == "S":
        sys.exit()
    else:
        print("Escolha uma opção válida")
        main()
main()