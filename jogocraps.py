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
    soma = somar()

    if soma == 7 or soma == 11:
        print("Ganhou")
    elif soma == 2 or soma == 3 or soma == 12:
        print("Perdeu")
    elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
        valor = soma
        valor = somar()
        while valor!= soma and valor!= 7:
            valor = somar()
            
        if valor == soma:
            print ("ganhou pela repeticao")
        
        elif valor == 7:
            print("perdeu pelo sete")
        
            


verificar()


        

            











    






                    
                   
        
      
                     




