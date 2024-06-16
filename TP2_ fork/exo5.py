import os, sys, time


# exercice 5 - TP2 : 

""" lit sur la ligne de commande (utiliser sys.argv) le nombre N de processus à créer.
 Il crée ces N processus en faisant N appels à os.fork().
 Il se met en attente (appel à pid_fils, etat = os.wait() ) de ces N processus fils et visualise
leur identité (pid_fils et la valeur de etat) au fur et à mesure de leurs terminaisons.
Chacun des processus fils Pi réalise le traitement suivant :
 Il visualise son pid (os.getpid()) et celui de son père (os.getppid()),
 Il se met en attente pendant 2*i secondes (time.sleep(2*i)) et visualise la fin de l'attente,
 Il se termine par sys.exit(i)
 """


# # python3 exo5.py 3

N = sys.argv[1]
N = int(N) 
for i in range (N) :
    pid = os.fork() 
    if (pid == 0) : 
        print(" je suis le processus fils :" ,os.getpid(),", mon pere est : ",os.getppid())
        time.sleep(2*i)
        os.exit(i)
        
for i in range (N) :
    pid, status = os.wait()
    etat = os.WEXITSTATUS(status)
    print("Mon fils", pid, "m'a reveillé et son état est", etat)
