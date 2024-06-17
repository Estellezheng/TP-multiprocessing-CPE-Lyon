from random import *
import os

# VERSION 2

# tubes nommés


""" Le premier processus génère N nombres aléatoires positifs ou nuls. Si le nombre généré est pair
(resp. impair) alors il est déposé dans le tube nombresPairs (resp. NnombresImpairs) - à la fin de la
génération, ce processus dépose la valeur -1 dans les 2 tubes (pour indiquer la fin de la série).
Ensuite il récupère les deux nombres stockés respectivement dans le tube sommePairs et
sommeImpairs, réalise leur somme et affiche le résultat. """



def generate_numbers(n, pipe_pairs_path, pipe_impairs_path):
    with open(pipe_pairs_path, 'w') as pipe_pairs, open(pipe_impairs_path, 'w') as pipe_impairs:
        for _ in range(n):
            number = random.randint(0, 100)
            if number % 2 == 0:
                pipe_pairs.write(f"{number}\n")     # fd = os.open("nombresPairs", os.O_WRONLY)
            else:
                pipe_impairs.write(f"{number}\n")
        
        pipe_pairs.write("-1\n")
        pipe_impairs.write("-1\n")

if __name__ == "__main__":
    N = 10
    pipe_pairs_path = "nombresPairs"
    pipe_impairs_path = "nombresImpairs"
    # os.mkfifo(pipe_pairs_path, 0o644)
    # os.mkfifo(pipe_impairs_path, 0o644)

    
    generate_numbers(N, pipe_pairs_path, pipe_impairs_path)
