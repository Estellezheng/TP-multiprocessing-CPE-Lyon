import os, sys

# exercice 6
#Combien de fois le message « 3ETI » sera-t-il affiché ?
#Dessinez un diagramme de séquence indiquant quelles lignes sont exécutées par chaque processus.
#Pour vous aider, vous pouvez rajouter des print() pour afficher notamment le PID retourné par
#os.getpid().

os.fork()
if (os.fork()) :   #pour le pere
    os.fork()
print("3ETI 2024")
sys.exit(0)


# 6 fois 3ETI
# il y a un grand père; 3 pères et deux fils
# GP : ligne 9 : crée P1 => ligne 10 : crée un P2 => ligne 11 : crée un P3 :print1
# P1 : ligne 10 : crée F1 => ligne 11 : crée F2 => print2
# P2 : print3
# P3 : print 4
# F1 : print5
# F2 : print6
