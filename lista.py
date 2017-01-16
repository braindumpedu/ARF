x = float(input("numero1 :"))
y = float(input("numero2 :"))
z= float(input("numero3 :"))


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
