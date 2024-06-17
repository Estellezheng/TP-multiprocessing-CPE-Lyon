
import os
import signal
import sys
import time
 

"""Reprendre  le  script  de  l'exercice  précédent et  le  modifier  pour  que  le  fils ne  fasse  ses 
affichages qu'à la réception du signal SIGUSR1. Le père envoie ce signal dans sa boucle à l’itération 3 et 
à l’itération 5. Il signale la fin du traitement au fils par envoi du signal SIGUSR2. 
Il n'y aura qu'une seule fonction d'interception dans le fils, elle recevra le numéro du signal déclencheur 
en paramètre"""


def interception(signum, frame):
    if signum == signal.SIGUSR1:
        print("Received SIGUSR1 in child process")
    elif signum == signal.SIGUSR2:
        print("Received SIGUSR2 in child process.")
        exit(0)


child_pid = os.fork()

if child_pid == 0:  
    signal.signal(signal.SIGUSR1, interception)  
    signal.signal(signal.SIGUSR2, interception) 
    while True:
        time.sleep(1)

else:  
    for i in range(6) :
        if i == 3 or i == 5 :
            print("Sending SIGUSR1 to child process")
            os.kill(child_pid, signal.SIGUSR1)   # envoi du signal 1
        else : 
            print(i)
        time.sleep(1)
    
    print("Sending SIGUSR2 to child process to indicate end of processing")
    os.kill(child_pid, signal.SIGUSR2)          # envoi du signal 2
    os.waitpid(child_pid, 0)                    # fin au process fils
