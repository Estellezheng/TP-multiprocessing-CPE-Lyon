import os, sys


# exercice 4

# Écrire deux programmes qui créent N processus Pi tels que :
# 1. Dans le 1 er programme : pour tout i entre 2 et N, P i soit le fils de Pi−1
# 2. Dans le 2 ème programme : pour tout i entre 2 et N, P i soit le fils de P1
# Chaque processus devra afficher son identifiant (son PID) et celui de son père. Dessinez l’arbre des processus
# correspondant à l’exécution de chacun des 2 programmes.
# Exemple d’affichage : Je suis le processus 1341, mon père est le processus 1339


# version 1
# le pere est à chaque fois tué

def creation_process(N):
    for i in range (2, N+1) :
        pid = os.fork()
        if pid == 0 :
            print("\nJe suis le processus", os.getpid(),"mon père est le processus", os.getppid())
        else:
            os.wait()  
            break

""" Je suis le processus 462 mon père est le processus 461
Je suis le processus 463 mon père est le processus 462
Je suis le processus 464 mon père est le processus 463
Je suis le processus 465 mon père est le processus 464
Je suis le processus 466 mon père est le processus 465
Je suis le processus 467 mon père est le processus 466
Je suis le processus 468 mon père est le processus 467 """
        

# version 2
# le fils est à chaque fois tué

def creation_process(N):
    for i in range (2, N+1) :
        pid = os.fork()
        if pid == 0 :
            print("\nJe suis le processus", os.getpid(),"mon père est le processus", os.getppid())
            break
        else:
            os.wait()  
        

""" Je suis le processus 589 mon père est le processus 588
Je suis le processus 590 mon père est le processus 588
Je suis le processus 591 mon père est le processus 588
Je suis le processus 592 mon père est le processus 588
Je suis le processus 593 mon père est le processus 588
Je suis le processus 594 mon père est le processus 588
Je suis le processus 595 mon père est le processus 588 """

if __name__ == "__main__" :
    N = 8
    creation_process(N)

