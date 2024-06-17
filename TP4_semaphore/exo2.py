import os
import sys
import multiprocessing as mp
import time


"""précédence de tâches
Un système est composé de deux tâches T1 et T2 soumises à
la contrainte de précédence T1 < T2. Ces deux tâches
appartiennent à deux processus P1 et P2 différents qui doivent
être synchronisés  Le processus P2 doit retarder
l’exécution de la tâche T2 jusqu’à ce que le premier
processus P1 termine la tâche T1"""

def process1(sem) :      
    print("P1; tache 1")    #effectue sa tache
    print("P1; tache 2")
    time.sleep(2)
    sem.release()   # relache et incrémente pour que 2 puisse travailler
    

def process2(sem) :       
    sem.acquire()   # decremente
    print("P2; tache 1")
    print("P2; tache 2")


if __name__ == "__main__" : 

    sem = mp.Semaphore(0)  # creation semaphore initilalisé à 1
  
    p1 = mp.Process(target = process1, args=(sem,))
    p2 = mp.Process(target = process2, args=(sem,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    
    sys.exit(0)