import os

lista = [3,4,5,1,4,6,7,8]
v = 6

def search(v,lista):
    nachei = True
    for a in lista:
        if a == v:
            nachei = False

    if nachei == False:
        print("Achei!")
    else:
        print("Não achei")


search(v,lista)

#for( int i = 0; i < n; i++ ){
#    printf("%d\n", lista[i]);
#}

if v in lista:
    print("Achei!")
else:
    print("Não achei!")