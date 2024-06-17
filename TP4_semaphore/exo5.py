import os
import sys
import multiprocessing as mp
import time
import random


""" Pour  réaliser  un  mécanisme  de  communication  un  à  plusieurs,  on  utilise  un  ensemble  de  processus  composé  
d’émetteurs et de récepteurs. Un émetteur produit un message (à simuler par l’affichage d’un message sur l’écran) 
et se met en attente jusqu’à ce qu’il y ait N-1 récepteurs au rendez-vous. Un récepteur lancé attend l’émission et 
l’arrivée des autres récepteurs.  Prenons l’exemple d’un rendez-vous 1 à 2 - On exécute ce script avec 4 récepteurs 
et 2 émetteurs : 
$> python exercice6 R E E R R R 
Voici un exemple des affichages de ce script :  
 
Le processus 1 récepteur se met en attente 
Le processus 2 émetteur produit un message et se met en attente 
Le processus 3 émetteur produit un message et se met en attente 
Le processus 4 récepteur débloque les processus 1 et 2 et consomme le message. 
Le processus 5 récepteur au Rendez-vous avec le processus 3 émetteur - Attente 
Le processus 6 récepteur débloque les processus 3 et 5.  """


def emetteur(semR,semE):
    mutex.acquire() #on protege pour qu'un seul emetteur accede aux 2 jetons recpteur
    print ("E franchi mutex")
    semR.acquire() # verif presence de deux recepteurs
    semR.acquire()  # verif presence de deux recepteurs
    print("E débloqué")
    semE.release() #creation jeton pour un recepteur
    semE.release() #creation jeton pour un recepteur
    mutex.release() #on reouvre le verrou
    
def recepteur(semR,semE):
    semR.release() #chaque recepteur créer un jeton 
    print("R la")
    semE.acquire() #chaque recepteur recupere un jeton emetteur
    print("R débloqué")
    
    
semE=mp.Semaphore(0)  #semaphore dans lequel l'emetteur met ses jetons
semR=mp.Semaphore(0) #semaphore dans lequel le recepteur met ses jetons
mutex=mp.Lock()
lp=[]
for arg in sys.argv :
    if arg=="R":
        R=mp.Process(target=recepteur, args=(semR,semE,))
        lp.append(R)
        R.start()
    if arg=="E":
        E=mp.Process(target=emetteur, args=(semR,semE,))
        lp.append(E)
        E.start()
        
for p in lp :
    p.join()