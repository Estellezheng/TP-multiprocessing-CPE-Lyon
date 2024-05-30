import os

# exercice 5
# fork() and wait()

#Ecrire un programme qui crée deux processus fils, l'un affiche les entiers de 1 à 100 et l'autre de 101 à 200.
#Modifier ce programme pour que les nombres s'affichent toujours dans l’ordre numérique croissant 1, 2, 3, ... ,
#200.

pid1 = os.fork()
if pid1 == 0 :          # fils1
    for i in range (101) :
        print( i, end=' ')
      
for _ in range (2):
    os.wait()

pid2 = os.fork()
if pid2 == 0 :          # fils2
    for i in (101, 201) :
        print( i, end=' ')
    
