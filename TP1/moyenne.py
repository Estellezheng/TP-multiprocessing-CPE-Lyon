# EXO 2

# alcule et affiche la moyenne d’un ensemble de notes (nombres
#entiers) passées en arguments sur la ligne de commande. Le résultat doit être affiché sous la forme :
# La moyenne sera affichée tronquée à 2 décimales de précision.

import sys

# $ python3 moyenne.py 10 15 15

total = 0
valide = 1
taille = len(sys.argv)-1 
if taille > 0 :
    for argument in sys.argv[1:] :
        if argument.isdigit() :
            argument = int(argument)
            if argument >= 0 and argument <=20 :
                total += argument
        else :
            valide = 0
            print("Note(s) non valide(s)")
else :
    print("Aucune moyenne à calculer")

if (valide):
    moyenne = total / taille
    moyenne = round(moyenne, 2)  
    print("Moyenne =", moyenne)     #print("%.2f" %x)
    