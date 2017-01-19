
import math 

def quadrado():
    x = int(input("Digite um número: "))
    while x != 0 :
        quadrado = math.pow(x, 2)
        print (x, quadrado)
        x = int(input("Digite um número: "))
        
    
        
       
    return quadrado

quadrado()









