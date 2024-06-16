import os, time


# exercice 3 - TP2 : os.fork() & os.exec()

#Ecrire un programme équivalent aux commandes shell suivantes :
# who & ps & ls –l Les commandes séparées par & s'exécutent simultanément [en parallèle].
# who ; ps ; ls -l Les commandes séparées par ; s'exécutent successivement [séquentiellement]



# Execution successive 

for i in range(2):
    pid = os.fork()
    if pid == 0:
        if i == 0:
            os.execlp("who", "who")
        elif i == 1:
            os.execl("/bin/ps", "ps")
            time.sleep(3)  # Attendre 3 secondes avant d'exécuter la prochaine commande
            os.execl("/bin/ls", "ls", "-l")

for _ in range(2):
    os.wait()


for i in range (3) :
    pid = os.fork()
    if pid == 0 :
        if (i == 0 and pid == 0):
            os.execlp("who","who")
        if (i ==1 and pid == 0) :
            os.execl("/bin/ps","ps")
        if (i ==2 and pid == 0) :
            os.execl("/bin/ls","ls","-l")

for _ in range(3):
    os.wait()


