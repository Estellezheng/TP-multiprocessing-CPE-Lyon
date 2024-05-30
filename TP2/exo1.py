import os, sys


# exercice 1 - TP2
#Ecrire un programme permettant d’exécuter deux processus, chacun réalisant son propre traitement. Tester la
# fonction os.execlp() en écrivant un programme qui lance un autre programme

def process1 ():
    print("programme 1 : id = ", os.getpid())
    os.execlp("python3", "python3", "exo1bis.py")

def process2 ():
    print("programme 2 : id = ", os.getpid())
    os.execlp("python3", "python3", "exo1bisbis.py")

if __name__ == "__main__":
    pid1 = os.fork()
    if pid1 == 0:
        process1()
    else: 
        process2()
