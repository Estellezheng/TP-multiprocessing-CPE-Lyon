import os, sys, time

# Réalisez un script montrant l’utilisation d’un tube anonyme (pipe) entre deux processu

msg = "monMessage"
msg = msg.encode()   # encode  str to byter
print("Création d'un pipe anonyme")

# creation
(dfr, dfw) = os.pipe()

# ecriture
n = os.write(dfw, msg)
print("Le processus %d a transmis le message %s \n" %(os.getpid(), msg))

# lecture
msgRecu = os.read(dfr, len(msg))
print("Le processus %d a recu le message %s \n" %(os.getpid(), msgRecu))

# fermeture
os.close(dfr)
os.close(dfw)

sys.exit(0)