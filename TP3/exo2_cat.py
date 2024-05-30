import os, sys, time


# commande cat texte.txt | wc


(dfr, dfw) =os.pipe()
pid = os.fork()

if pid !=0 :    #père ecrit
    os.close(dfr)
    print ("[Le processus %d] : cat \n" % os.getpid())
    os.dup2(dfw,1)  #copie l'entrée vers la sortie
    os.close(dfw)
    os.execlp("cat", "cat", "texte.txt")
else :          #fils lit
    os.close(dfw)
    print("[Le processus %d] : wc \n" % os.getpid())
    os.dup2(dfr,0)  #copie la sortier vers l'entree
    os.close(dfr)
    os.execlp("wc", "wc", "texte.txt")

sys.exit(0)