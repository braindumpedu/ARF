import random
import time

def somar():
    soma = int()
    numero = random.randint(1,6)
    numero1 =  random.randint(1,6)
    soma = numero + numero1
    print(soma)
    
    return soma

def verificar():
    print("Lancando os dados pela primeira vez..")
    time.sleep(3)
    soma = somar()

    if soma == 7 or soma == 11:
        print("Ganhou")
    elif soma == 2 or soma == 3 or soma == 12:
        print("Perdeu")
    elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
        valor = soma
        valor = somar()
        while valor!= soma and valor!= 7:
            variavel = somar()

            if variavel == valor:
                    print ("ganhou pela repeticao")
            elif variavel== 7:
                    print("perdeu pelo sete")
            if variavel  == valor or variavel == 7:
                break


verificar()


        

            











    






                    
                   
        
      
                     




