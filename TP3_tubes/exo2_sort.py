import os, sys, time


# commande sort < fichier | grep chaine | tail –n 5 > sortie


entree = 'texte'
sortie = 'sortie'

(dfr1, dfw1) =os.pipe()
(dfr2, dfw2) =os.pipe()

pid1 = os.fork()

if pid1 !=0 :    #père ecrit
    os.close(dfr1)
    input = os.open(entree, os.O_RDONLY)
    os.dup2(dfw1,1)  #copie l'entrée vers la sortie
    os.dup2(input, 0)
    os.close(dfw1)
    os.execlp("sort", "sort")

else :          #fils lit
    pid2 = os.fork()

    if pid2 !=0 : 
        os.close(dfw1)
        os.close(dfr2)
        os.dup2(dfr1,0)  #copie la sortier vers l'entree
        os.dup2(dfw2,1)  
        os.close(dfr1)
        os.close(dfw2)
        os.execlp("grep", "grep", "toto")

    else :   #petit fils  ecrit
        os.close(dfw2)
        os.dup2(dfr2,0)  #copie la sortier vers l'entree
        os.close(dfr2)
        output = os.open(sortie, os.O_WRONLY | os.O_TRUNC | os.O_CREAT, 0o644 )
        os.dup2(output,1)
        os.close(output)
        os.execlp("tail", "tail", "-n 5")
    



sys.exit(0)