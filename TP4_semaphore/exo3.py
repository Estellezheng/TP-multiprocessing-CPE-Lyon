import os
import sys
import multiprocessing as mp
import time
import random

"""rendez-vous de deux processus
On considère deux processus producteurs P1 et P2 qui produisent des messages (nombres entiers tirés
aléatoirement) et les déposent dans deux queues (files message vues en cours) Q1 et Q2 respectivement (Qi pour
Pi , i=1,2). 
Deux processus consommateurs C1 et C2 consomment les messages : C1 ceux déposés dans Q1 , C2 ceux
déposés dans Q2 ; avec la contrainte que lorsqu’un processus Ci (i=1,2) consomme un message, il attendra que
l’autre processus Cj (j=3-i) ait consommé un message lui aussi pour continuer à consommer un autre message
(Rendez-vous entre C 1 et C2 après chaque consommation). Synchroniser ces processus en utilisant les
sémaphore"""


def producteur1 (N) : 
    for i in range (N):
        val = random.randint(0,9)    
        Q1.put(val)
        print(f"producteur 1 : {val}")

def producteur2 (N) : 
    for i in range (N):
        val = random.randint(0,9)    
        Q2.put(val)
        print(f"producteur 2 : {val}")

def consommateur1(N) : 
    for i in range (N):  
        val = Q1.get()
        print("consommateur 1", val)
        time.sleep(1)

        rdv_c1.release() 
        rdv_c2.acquire()  
        
        
def consommateur2(N) :     
    for i in range (N):  
        rdv_c2.release()
        val = Q2.get()
        print("consommateur 2", val)
        time.sleep(2)
        rdv_c1.acquire()
        

if __name__ == "__main__" : 

    N = 10
    rdv_c1 = mp.Semaphore(0)  # creation semaphore initilalisé à 1
    rdv_c2 = mp.Semaphore(0)
    
    p1 = mp.Process(target = producteur1, args=(N,))
    p2 = mp.Process(target = producteur2, args=(N,))
    c1 = mp.Process(target = consommateur1, args=(N,))
    c2 = mp.Process(target = consommateur2, args=(N,))

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

