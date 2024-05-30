import os
import signal
import sys
import time
 
"""Modifiez le programme précédent pour qu'il fasse son affichage dans une boucle
conditionnée par une variable booléenne fin initialisée à False et qui sera mise à True par la fonction
d'interception du signal."""


global fin  
fin = False


def ignore (signal, frame) :
    global fin 
    fin = True
    print ("fin")

    
signal.signal(signal.SIGINT, ignore)
print(fin)

if (os.fork !=0) :
    while fin == False:
        print ("Je boucle")
        time.sleep(1)
