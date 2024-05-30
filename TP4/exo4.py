import os
import sys
import multiprocessing as mp
import time
import random


"""Rendez-vous à 2 et à 3 
Deux processus P1 et P2 souhaitent établir un rendez-vous avant l’exécution de la fonction rdv1() pour l’un et
rdv2() pour l’autre. En utilisant les sémaphores, écrire les scripts P1 et P2 permettant d’établir ce rendez-vous.
 Rendez-vous à 2 et à 3 : Réaliser un rendez-vous entre 3 processus P1, P2 et P3."""


def process1 (N) : 
    print("process1")


def producteur2 (N) : 
    for i in range (N):
        val = random.randint(0,9)    
        Q2.put(val)
        print("2", val)
        



if __name__ == "__main__" : 

    N = 10
    rdv_c1 = mp.Semaphore(0)  # creation semaphore initilalisé à 1
    rdv_c2 = mp.Semaphore(0)
    
    p1 = mp.Process(target = producteur1, args=(N,))
    p2 = mp.Process(target = producteur2, args=(N,))


    Q1 = mp.Queue()
    Q2 = mp.Queue()

    p1.start()
    p2.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    c1.join()
    c2.join()

    
    sys.exit(0)


