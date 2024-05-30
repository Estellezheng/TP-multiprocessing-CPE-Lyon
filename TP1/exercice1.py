import sys

# EXO 1
# python3 /home/estelle.zheng/Documents/TP1.py  python 3 ETI 2024

print("Nom du programme : ", sys.argv[0])
print("Nombre d’arguments : ", len(sys.argv)-1)
print("Les arguments sont : ")
for argument in sys.argv[1:] :
    print(argument)


# EXO 2
