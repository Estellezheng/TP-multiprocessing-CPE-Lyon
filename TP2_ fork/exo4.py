import os, sys


# exercice 4 - TP2 : 


n=0
for i in range(1,5) :
    fils_pid = os.fork() #1
    if (fils_pid > 0) : #2
        os.wait() #3
        n = i*2
        break
print("n = ", n) #4
sys.exit(0)


# ligne 2 : dans le if on se trouve dans le process père / la valeur fils_pid est nulle pour le fils

# le programme est (pas) deterministe puisque quand il rentre dans la boucle os.wait attend la fin du processus de son enfant donc il y a 4 membres, 
#le dernier enfant s'affiche en premier (8) et en dernier le père (2)

# en supprimant la ligne 3 os.wait(), le programme est déterministe, mais c'est le premier parent qui s'affiche en premier et le dernier enfant qui s'affiche en dernier

# 0 8 6 4 2
