import os, sys


# exercice 4

# Écrire deux programmes qui créent N processus Pi tels que :
# 1. Dans le 1 er programme : pour tout i entre 2 et N, P i soit le fils de Pi−1
# 2. Dans le 2 ème programme : pour tout i entre 2 et N, P i soit le fils de P1
# Chaque processus devra afficher son identifiant (son PID) et celui de son père. Dessinez l’arbre des processus
# correspondant à l’exécution de chacun des 2 programmes.
# Exemple d’affichage : Je suis le processus 1341, mon père est le processus 1339


def creation_process(N):
    for i in range (2, N+1) :
        pid = os.fork()
        # processid = 0 represents the created child process
        if pid == 0 :
            print("\nJe suis le processus", os.getpid(),"mon père est le processus", os.getppid())
            break
        
if __name__ == "__main__" :
    N = 8
    creation_process(N)