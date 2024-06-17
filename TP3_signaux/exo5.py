
import os
import signal
import sys
import time
 

"""Recopier le script précédent et le modifier pour que le père n'envoie plus ce signal au fils 
mais que le fils intercepte tous les SIGINT en affichant un message d'interception. 
Exécutez alors le programme et interrompez le par un ^C : Que constatez-vous? Expliquez pourquoi. 
(Pour vous aider, utilisez la commande ps –l"""


def interception(signal, frame) :
    print("interception du signal")
    sys.exit(0)

def child_process():
    """Processus fils qui affiche un message dans une boucle infinie."""
    signal.signal(signal.SIGINT, interception)
    while True:
        print("Fils: En cours...")
        time.sleep(1)

def parent_process(child_pid):
    """Processus père qui affiche un message dans une boucle et tue le fils après 3 itérations."""
    for i in range(3):
        print(f"Père: Compteur = {i}")
        time.sleep(1)


if __name__ == "__main__":

    pid = os.fork()
    if pid > 0:
        parent_process(pid)
    else :
        child_process()
