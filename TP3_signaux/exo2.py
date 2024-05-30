import os
import signal
import sys
import time


"""Modifier le programme précédent pour qu'il ignore le signal SIGINT. Lancez-le en tâche de
fond (python3 exo2.py &). Essayez de l'interrompre avec un ^C. Que constatez-vous ?
Pour le supprimer, il faut lancer la commande ps –l pour obtenir l’identifiant du Processus (PID) et
lancer la commande : kill -9 numProcessus (Vous pouvez remplacer 9 par SIGKILL)."""


def ignore (signal, frame) :
    print ("reception du signal")

signal.signal(signal.SIGINT, ignore)

if (os.fork !=0) :
    
    while True :
        print ("Je boucle")
        time.sleep(1)