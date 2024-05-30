# EXO 1
# traite plusieurs arguments


import sys

# $ python3 miroir2.py ecart DNA saper
# trace AND repas

for argument in sys.argv[1:] :
    print( "".join(reversed(argument)), end=' ')  