import os, time, random, sys


# Sans modifier les lignes de 2 à 7, modifiez ce programme de façon à ce que les processus fassent leur
# affichage par ordre alphabétique inversé du nom : D D C B A

for i in range(4) :
    if os.fork() != 0 :
        break
random.seed()
delai = random.randint(1,4)
time.sleep(delai)

try : 
    os.wait() 
except :
    pass
print("Mon nom est " + chr(ord('A')+i) + " j ai dormi " + str(delai)+ " secondes")

sys.exit(0)



#1 il y a 5 membres dans l'arbre généaogique

#2 Les affichage possibkes
# nom : entre A et D
    # chr(ord('A')+i)       ord(A) = 65     => ord('A')+i entre 65 et 68        => chr(ord('A')+i) entre A et D
# délai : entre 0 et 4