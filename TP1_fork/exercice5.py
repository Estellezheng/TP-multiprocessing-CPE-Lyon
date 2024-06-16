import os

# exercice 5
# fork() and wait()

#Ecrire un programme qui crée deux processus fils, l'un affiche les entiers de 1 à 100 et l'autre de 101 à 200.
#Modifier ce programme pour que les nombres s'affichent toujours dans l’ordre numérique croissant 1, 2, 3, ... ,
#200.

def child_process(start, end):
    for i in range(start, end + 1):
        print(i)

if __name__ == "__main__":
    pid1 = os.fork()
    if pid1 == 0:
        child_process(1, 100)
        os._exit(0)  # Ensure the child process exits after finishing

    else:
        # Parent process: wait for the first child to finish
        os.waitpid(pid1, 0)

        pid2 = os.fork()
        if pid2 == 0:
            child_process(101, 200)
            os._exit(0)  

        else:
            os.waitpid(pid2, 0)