import os
import signal
import sys
import time

"""Ecrire un programme qui réalise un affichage dans une boucle infinie, mais qui prévoit de
s'arrêter à la réception du signal SIGINT. La fonction d'interception [de déroutement] affichera un message
signalant la réception du signal avant de terminer le programme par un appel à sys.exit()"""


def interception (signal, frame) :
    print ("reception du signal")
    sys.exit(0)

signal.signal(signal.SIGINT, interception)

while True :
    print ("Je boucle")
    time.sleep(1)