# EXO 1
# Ecrivez un programme (miroir.py) qui prend en argument une chaîne de caractères et l’affiche à l’envers

import sys

# python3 miroir.py trace

mot = sys.argv[1]
print(mot)
print( "".join(reversed(mot)))  