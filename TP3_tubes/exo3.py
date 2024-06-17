import os
from random import *


""" Transmettre un float via pipe en python extrêment complexe du fait de choix de python
sur les variables à longueur dynamique """


""" var = 12.5
piper,pipew = os.pipe()
#conversion de var en hexadecimal et encoder en byte pour être transmis sur un pipe
var_b = var.hex().encode()
#soucis on ne connais pas la longueur du tableau de byte en lecture du coup
#on crée un petit protocole d'échange
#| 4 octets | length octets |
#| length   | data          |
length = len(var_b)
#conversion de la taille en octet: 4 octet, little endian (architecture x86) peut être dans certain cas big endian
# signed=True si la valeur peut être négative
lb = length.to_bytes(4,byteorder="little",signed = True)
#écriture de la taille sur 4 octet
os.write(pipew,lb)
#ecriture des données
os.write(pipew,var_b)

#Lecture de la taille 4 octet
lb = os.read(piper,4)
#conversion inverse pour obtenir un entier "python", la taille (4) est déduite de la taille du contenu de lb
length = int.from_bytes(lb,byteorder="little",signed=True)
#lecture des données de longueur lengthos.write(dfw1, i)
var_b = os.read(piper,length)
# conversion des données de bytes vers str (decode) puis conversion de str contenant de l'hexa vers float
var = float.fromhex(var_b.decode())
print(var) """


'''
Soucis inexistant en C, par exemple, on écrit/lit le float directement avec write/read
sans avoir besoin de s'embêter

float var = 3.5;
write(pipew,&var,sizeof(var));
float var_read=0;
read(piper,&var_read,sizeof(var));
'''


""" Le premier processus génère N nombres aléatoires positifs ou nuls. Si le nombre généré est pair
(resp. impair) alors il est déposé dans le tube nombresPairs (resp. NnombresImpairs) - à la fin de la
génération, ce processus dépose la valeur -1 dans les 2 tubes (pour indiquer la fin de la série).
Ensuite il récupère les deux nombres stockés respectivement dans le tube sommePairs et
sommeImpairs, réalise leur somme et affiche le résultat.

2. Un deuxième processus est chargé de réos.write(dfw1, i)cupérer les nombres stockés dans le tube nombresPairs, de
réaliser la somme de ces nombres et de déposer le résultat dans le tube SommePairs.

3. Un troisième processus est chargé de récupérer les nombres stockés dans le tube nombresImpairs, de
réaliser la somme de ces nombres et de déposer le résultat dans le tube sommeImpairs
 """

# Version 1 : Un script Python composé de 3 processus réalisant les traitements demandés en utilisant les

# tubes ANONYMES.

N = 10
(dfr1, dfw1) =os.pipe()  #impair
(dfr2, dfw2) =os.pipe()  #pair

(SPR, SPW) =os.pipe()  #impair
(SIR, SIW) =os.pipe()  #pair

for i in range (N) : 
    nombre = randint(1, 10)
    nombre = float(nombre)
    nombre_b = nombre.hex().encode()
    length = len(nombre_b)
    lb = length.to_bytes(4,byteorder="little",signed = True)

    if nombre % 2 == 0 :    # nbr pair
        os.write(dfw2,lb)
        os.write(dfw2,nombre_b)
    else :
        os.write(dfw1,lb)
        os.write(dfw1,nombre_b)

    if i==N-1 :
        val_final = -1
        val_final = float(val_final)
        val_final_b = val_final.hex().encode()
        length = len(val_final)
        lb = length.to_bytes(4,byteorder="little",signed = True)
        os.write(dfw2,lb)
        os.write(dfw2,val_final_b)
        os.write(dfw1,lb)
        os.write(dfw1,val_final_b)
        



# Version 2 ; Trois scripts Python correspondant à 3 processus indépendants (generateurNombres.py, filtrePair.py
# et filtreImpair.py) réalisant les traitements demandés en utilisant les tubes nommés