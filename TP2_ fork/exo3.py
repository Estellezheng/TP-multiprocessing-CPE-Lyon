import os, time


# exercice 3 - TP2 : os.fork() & os.exec()

#Ecrire un programme équivalent aux commandes shell suivantes :
# who & ps & ls –l Les commandes séparées par & s'exécutent simultanément [en parallèle].
# who ; ps ; ls -l Les commandes séparées par ; s'exécutent successivement [séquentiellement]



# Execution successive 

for i in range (3) :
    pid = os.fork()
    if (i == 1 and pid == 0):
        os.execlp("who","who")
    if (i ==2 and pid == 0) :
        os.execl("/bin/ps","ps")
    if (i ==2 and pid == 0) :
        os.execl("/bin/ls","ls","-l")

# Execution silmutannée

for i in range (3) :
    pid = os.fork()
    time.sleep(3)
    if (i == 1 and pid == 0):
        os.execlp("who","who")
    if (i ==2 and pid == 0) :
        os.execl("/bin/ps","ps")
    if (i ==2 and pid == 0) :
        os.execl("/bin/ls","ls","-l")

