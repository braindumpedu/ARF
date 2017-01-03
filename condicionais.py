def ler_temperatura():
    #Ler a temperatura de uma pessoa e exibir amensagem “Febre Alta” (temp ≥ 39), “Febril”(39 > temp ≥ 37) ou “Sem Febre” (temp <37)
    T = input("Temperatura: ")
    T = float(T)
    if T >= 39.0:
        print("Febre Alta, vai morrer")
    elif 37.8 <= T and T <= 39.0:
        print("Febre baixa, tomara que morra")
    elif T <= 35.5:
        print("Hipotermia, tambem vai morrer")
    else:
        print("Afebril, tomara que morra tambem")

def ler_par():
    #Ler um número inteiro de dizer se é par ou ímpar.. primeiro exercício em Python que fiz!! Uhuuuuuuuullllll
    N = input("Pár ou ímpar: ")
    N = int(N)

    if N % 2 == 0:
        print( "eu sou um numero par")
    else:
        print( "eu sou um numero impar")

def calcular_velocidade():
    D = input("Distância percorrida em km: ")
    D = float(D)
    T = input("Tempo em horas: ")
    T = float(T)

    V = D/T
    print(V)

    if V >= 110:
        print("Velocidade Media Superior ao Limite Determinado" )
    else:
        print("Nao ultrapassou o limite de velocidade media")

def ler_bissexto():
    #Faça um Programa que peça para entrar com um ano (inteiro com 4 dígitos) e determine se o mesmo é ou não bissexto (divisível por 4).
    A = input("Bissexto?: ")
    A = int (A)

    if A % 4 == 0:
        print("Olá Pessoal! Eu sou um ano Bissexto!")
    else:
        print("Nao sou SaoPaulino")

def calcular_media():
    #Ler do usuario numeros até que a entrada seja -1 e devolver a media dos numeros inseridos
    pass

escolha = 0
while escolha != -1:
    escolha = int(input("Escolha sua função: "))
    if escolha == 0:
        ler_temperatura()
    elif escolha == 1:
        ler_par()
    elif escolha == 2:
        calcular_velocidade()
    elif escolha == 3:
        ler_bissexto()
    elif escolha == -1:
        print("Adeus")
    else:
        print("Escolha inválida")
