import math

def distancia(ponto1, ponto2):
   d = math.sqrt(math.pow(ponto1[0]-ponto2[0],2) + math.pow(ponto1[1]-ponto2[1],2))

   return d 
    
def perimetroTriangulo(p1, p2, p3):
    
    lado1 = distancia(p1, p2)
    lado2 = distancia(p1, p3)
    lado3 = distancia(p2, p3)

    return lado1 + lado2 + lado3

def perimetroTriangulo1(l):
    lado1 = distancia(l[0], l[1])
    lado2 = distancia(l[0], l[2])
    lado3 = distancia(l[1], l[2])

    return lado1 + lado2 + lado3

def perimetroQuadrado(p1, p2, p3, p4):
    lado1 = distancia(p1, p2)
    lado2 = distancia(p2, p3)
    lado3 = distancia(p3, p4)
    lado4 = distancia(p1, p4)

    return lado1 + lado2 + lado3 + lado4

def perimetroPentagono(p1, p2, p3, p4, p5):
    lado1 = distancia(p1, p2)
    lado2 = distancia(p2, p3)
    lado3 = distancia(p3, p4)
    lado4 = distancia(p4, p5)
    lado5 = distancia(p1, p5)

    return lado1 + lado2 + lado3 + lado4 + lado5


print(perimetroQuadrado([4.0, 0.0], [4.0, 4.0], [0.0, 4.0], [0.0, 0.0]))

print(perimetroTriangulo([4.0, 0.0], [3.0, 6.0], [8.0, 16.0]))

print(perimetroPentagono([4.0, 0.0], [4.0, 4.0], [0.0, 4.0], [5.0, 9.0], [18.0, 12.0]))

print(perimetroTriangulo1([[4.0, 0.0], [3.0, 6.0], [8.0, 16.0]]))





