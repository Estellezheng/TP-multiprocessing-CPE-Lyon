from random import *
import os


""" Le premier processus génère N nombres aléatoires positifs ou nuls. Si le nombre généré est pair
(resp. impair) alors il est déposé dans le tube nombresPairs (resp. NnombresImpairs) - à la fin de la
génération, ce processus dépose la valeur -1 dans les 2 tubes (pour indiquer la fin de la série).
Ensuite il récupère les deux nombres stockés respectivement dans le tube sommePairs et
sommeImpairs, réalise leur somme et affiche le résultat. """


N = 10
pair ="nombresPairs"
impair ="NnombresImpairs"
os.mkfifo(pair, 0o644)
os.mkfifo(impair, 0o644)

for i in range (N) : 
    nombre = randint(0,100)
    if nombre % 2 == 0 :    # nbr pair
        fd = os.open("nombresPairs", os.O_WRONLY)
        print(fd)
