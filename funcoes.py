import random
import time

def displayIntro():
    print("You are in a land full of dragons. In front You,")
    print("you see two caves. In on cave, the dragon is friendly")
    print("and will share his treasure with you. The other dragon")
    print("is greedy and hungry, and will eat you on sight.")
    print()

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("caverna 1 ou 2?")
        cave = input()
    
    return cave

def checkCave(chooseCave):
    print("Entrando na caverna...")
    time.sleep(2)
    print("La vem o dragao...")
    time.sleep(2)
    print("O dragao apareceu na sua frente.. e Agora??")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chooseCave == str(friendlyCave):
        print("Escolha certa. Dragao amigo.. Ganhou!!")
    
    else: 
        print("Perdeu.. O dragao vai comer vc!!")
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    
    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print("Quer jogar de novo? Sim ou nao?")
    playAgain = input()

    