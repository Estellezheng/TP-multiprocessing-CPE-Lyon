
import os
import signal
import sys
import time
 

"""Ecrire un programme composé de 2 processus : Le père fait des affichages toutes les
secondes dans une boucle for et le fils fait des affichages toutes les secondes aussi mais dans une boucle
infinie. Quand le compteur de boucle du père arrive à 3, le père envoie un signal SIGKILL au fils. On a
constaté dans l'exercice 2, l'impossibilité d'ignorer ce signa"""