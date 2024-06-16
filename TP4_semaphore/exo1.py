import os
import sys
import multiprocessing as mp



"""pour calculer la somme des éléments d’une liste L à N entiers on utilise deux processus qui s’exécutent en
parallèle. Le processus P1 parcourt les éléments d’indice impair et le processus P2 parcourt les éléments d’indice
pair. Le processus père lance les 2 processus P1 et P2. A la fin d’exécution de P1 et P2, le processus père affiche
le résultat stocké dans la variable partagée Somme."""

def process1(N, liste) :        # somme impaire
    i =1
    sommeImpaire = 0
    while(i<N) :
        sommeImpaire += liste[i]
        i += 2
    sem.acquire()
    somme.value += sommeImpaire
    sem.release()
    sys.exit(0)

def process2(N, liste) :        # somme paire
    i =0
    sommePaire = 0
    while(i<N) :
        sommePaire += liste[i]
        i += 2
    sem.acquire()
    somme.value += sommePaire
    sem.release()
    sys.exit(0)


if __name__ == "__main__" : 

    liste = [1,2,3,4,5,6,7]
    N = len(liste)

    sem = mp.Semaphore(1)  # creation semaphore initilalisé à 1
    somme = mp.Value('i',0) # variable partagée

    p1 = mp.Process(target = process1, args=(N, liste))
    p2 = mp.Process(target = process2, args=(N, liste))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(somme.value)
    
    sys.exit(0)