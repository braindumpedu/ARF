

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

def valorMinimo (l):
    menorValor = 34534
    for n in l :
        if n < menorValor:
            menorValor = n 
    return( menorValor)

def valorMaximo (l):
    maiorValor = -34534 # sentinela
    for n in l :
        if n > maiorValor:
            maiorValor = n 
    return (maiorValor)

def busca (l , v ):
    for n in l :
        if n == v:
            return True 
    return False

preco = 0
l = []
while preco >= 0:
    preco = float(input("preco:"))
    if preco >=  0:
        l.extend([preco])

m = valorMinimo(l)
print("Menor Valor",(m))
print(l)

print(min(l))

l = input("listadeprecos").split()
print (l)


#acessando elementos da lista
#print(l[0], l[1], l[2])
#recebendo numero de elementos da lista
#print(len(l))

#extendendo a lista com outra lista
#l.extend([4,5,67])
#print(l)
#print(len(l))

