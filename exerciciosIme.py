
import math 

def quadrado():
    x = 1
    l = []
    while x != 0 :
        quadrado = math.pow(x, 2)
        print (x, quadrado)
        x = int(input("Digite um número: "))
        l = input("listaNumeros").split()
        print (l)
       
        
    return quadrado

quadrado()












