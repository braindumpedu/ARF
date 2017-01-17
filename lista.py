x = float(input("numero1 :"))
y = float(input("numero2 :"))
z = float(input("numero3 :"))

def imprimir_menor_por_comparacao(x , y, z):
    if x < y and x < z :
        print (x)
        if y < z :
            print (y)
            print (z)
        else: 
            print (z)
            print (y)
    elif y < x and y < z:
        print (y)
        if x < z :
            print (x)
            print (z)
        else: 
            print (z)
            print (x)

    else:
        print (z)
        if x < y :
            print(x)
            print(y)
        else:
            print(y)
            print(x)

#definindo a lista
l = [x, y, z]
#print(l)

#acessando elementos da lista
#print(l[0], l[1], l[2])
#recebendo numero de elementos da lista
#print(len(l))

#extendendo a lista com outra lista
l.extend([4,5,67])
#print(l)
#print(len(l))
