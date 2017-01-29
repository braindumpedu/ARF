# Jogo da Forca #

def palavra():
    palavraSecreta = [ "T", "A", "I", "N", "A"]
    letrasDescobertas = []

    print("\n*** DESCUBRA A PALAVRA SECRETA ***\n")

    for i in range(0, len(palavraSecreta)):
        letrasDescobertas.append("-")

    acertou = False

    while acertou == False :
        letra = str(input("DIGITE UMA LETRA  "))

        for i in range(0, len(palavraSecreta)):
            if letra == palavraSecreta[i]:
                letrasDescobertas[i] = letra

            print(letrasDescobertas[i])
        
        acertou = True

        for x in range(0, len(letrasDescobertas)):
            if letrasDescobertas[x] == "-":
                acertou = False
            
            
    print("PARABENS, VC COMPLETOU A PALAVRA")
  
novojogo = "Sim"

while novojogo == "Sim" or novojogo == "sim":
    palavra()
    print("Quer jogar novamente? Digite Sim!")
    novojogo = input() 