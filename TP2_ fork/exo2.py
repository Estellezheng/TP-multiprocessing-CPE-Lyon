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

""" 
i :  0 ; je suis le processus : 1091 , mon pere est :  1090 , retour :  1092 
i :  0 ; je suis le processus : 1092 , mon pere est :  1091 , retour :  0 
i :  1 ; je suis le processus : 1092 , mon pere est :  1091 , retour :  1093 
i :  1 ; je suis le processus : 1091 , mon pere est :  1090 , retour :  1094 
i :  1 ; je suis le processus : 1093 , mon pere est :  1092 , retour :  0 
i :  1 ; je suis le processus : 1094 , mon pere est :  1091 , retour :  0 
i :  2 ; je suis le processus : 1092 , mon pere est :  1091 , retour :  1095 
i :  2 ; je suis le processus : 1093 , mon pere est :  1092 , retour :  1096 
i :  2 ; je suis le processus : 1091 , mon pere est :  1090 , retour :  1097 
i :  2 ; je suis le processus : 1094 , mon pere est :  1091 , retour :  1098 
i :  2 ; je suis le processus : 1097 , mon pere est :  1091 , retour :  0 
i :  2 ; je suis le processus : 1096 , mon pere est :  1093 , retour :  0 
i :  2 ; je suis le processus : 1098 , mon pere est :  1094 , retour :  0 
  """