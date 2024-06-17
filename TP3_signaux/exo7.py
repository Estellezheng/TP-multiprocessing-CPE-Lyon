import signal
import time


""" Ecrire un script qui demande à l'utilisateur de taper au clavier un entier en moins de 5
secondes. Pour cela, votre programme ne doit pas "planter" si l’utilisateur n’a pas saisi un nombre
entier. Il devra donc lire une chaîne de caractères et tenter de la convertir en un entier, si c'est bon il se
terminera après avoir désarmé le time Out, sinon il recommencera éventuellement jusqu'aux 5 secondes
où il affichera "trop tard" avant de s'arrêter.
Exemples :
Entrez un entier en moins de 5 secondes
Svp un entier : a
Svp un entier : x
Svp un entier : 12
Ok merci !!

Entrez un entier en moins de 5 secondes
Svp un entier : E
Svp un entier : f
Svp un entier : D
Trop tard !! """

def alarme(signum, frame):
    print("Trop tard !!")
    exit(1)

signal.signal(signal.SIGALRM, alarme)

print("Entrez un entier en moins de 5 secondes")
print("Svp un entier : ", end='')

for _ in range(5):
    try:
        signal.alarm(5)  # Déclenche une alarme après 5 secondes
        user_input = input()
        signal.alarm(0)  # Désactive l'alarme si une entrée a été reçue avant la fin du délai
        integer_value = int(user_input)
        print("Ok merci !!")
        exit(0)
    except ValueError:
        print("Svp un entier : ", end='')

print("Trop tard !!")