import random
import time

def somar():
    numero = random.randint(1,6)
    numero1 =  random.randint(1,6)
    soma = numero + numero1
    print(soma)
    
    return soma

def verificar():
    print("Primeiro lancamento de dados")
    time.sleep(3)
    soma = somar()

    if soma == 7 or soma == 11:

        print("Acertou!")

    elif soma == 2 or soma == 3 or soma == 12:
        print("Perdeu de cara!!")

    elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
        valor = soma
        print("Segundo lancamento de dados...")
        time.sleep(3)
        valor = somar()
        while valor!= soma and valor!= 7:
            print("Jogando dados dentro do While..")
            time.sleep(3)
            valor = somar()
            
        if valor == soma:
            print ("Ganhou pela repeticao!!" )
        
        elif valor == 7:
            print("perdeu pelo sete ")


novojogo = "Sim"

while novojogo == "Sim" or novojogo == "sim":
    verificar()
    print("Quer jogar novamente? Digite Sim!")
    novojogo = input()       



        

            











    






                    
                   
        
      
                     




