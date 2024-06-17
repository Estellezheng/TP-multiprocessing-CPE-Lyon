import os, sys, time

# Réalisez un script montrant l’utilisation d’un tube anonyme (pipe) entre deux processu

msg = "monMessage"
msg = msg.encode()   # encode  str to byter

# creation
(dfr, dfw) = os.pipe()      # out, in
print("Création d'un pipe anonyme")

# ecriture
os.write(dfw, msg)
print(f"Le processus {os.getpid()} a transmis le message {msg}")

# lecture
msgRecu = os.read(dfr, len(msg))
print(f"Le processus {os.getpid()} a recu le message {msgRecu}")

# fermeture
os.close(dfr)
os.close(dfw)

sys.exit(0)