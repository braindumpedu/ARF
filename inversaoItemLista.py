# Faca um programa que leia uma lista e 10 numeros reais e mostre- os na ordem inversa:
import time
def lista():
    valor = float(1.0)
    l = []

    while len(l) < 5:
        valor = float(input("Digite um numero real: "))
        l.append([valor])

    l.reverse()
    print(l)
    
novo = "sim"

while novo == "sim" or novo == "Sim":
    print("Aguarde 2 segundos")
    time.sleep(2)
    lista()
    time.sleep(1)
    print("Deseja digitar novamente???")
    novo = str(input())
    
   


    
    
