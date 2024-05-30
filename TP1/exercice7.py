import os, sys

# exo 7
# Dessinez l’arbre généalogique des processus engendrés par le programme ci-dessous.


if (os.fork() != 0) :
    if (os.fork() == 0) :
        os.fork()
        print("1")
    else :
        print("2")
else :
    print("3")
print("4")
sys.exit(0)


# il afffiche : 2 4 3 4 1 4 1 4
# GP : ligne 7 : crée P1 => ligne 8 (père): crée P2 => print 2, 4
# P1 : départ ligne 7 (fils) => ligne 13 : print 3, 4
# P2 : départ ligne 8 : crée un fils => print 
