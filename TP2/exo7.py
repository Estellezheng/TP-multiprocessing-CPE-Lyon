import os, sys


# exercice 7 - TP2 : 

""" Ajoutez des instructions permettant de gérer les processus
nécessaires pour provoquer l'affichage du message «Bonjour» exactement 4N fois. Vous ne pouvez pas insérer
du code supplémentaire ailleurs qu'à l'endroit indiqué et vous ne pouvez plus ajouter d'instructions print().
Vous devez donner une solution utilisant des os.fork(), avec éventuellement des sys.wait() """


N = 3
for i in range(N) :
    #__________début des ajouts_________
    pid = os.fork()
    if (pid!=0) :
        os.wait()
    else :
        os.fork()
    


    # __________fin des ajouts__________
print("Bonjour")
sys.exit(0)
