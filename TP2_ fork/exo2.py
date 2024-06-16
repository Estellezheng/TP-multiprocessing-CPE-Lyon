import os


# exercice 2 - TP2 : appel à fork() dans une boucle
#Ecrire un programme qui fait appel à la fonction os.fork() dans une boucle for i in range(3).
#A chaque itération le programme affichera les informations suivantes :
#(i : valeur_de_i) je suis le processus : pid, mon pere est : ppid, retour : retour

for i in range(3):
    retour = os.fork()
    pid = os.getpid()
    ppid = os.getppid()
    print("i : ", i ,"; je suis le processus :" ,pid,", mon pere est : ",ppid,", retour : ",retour,"")