import numpy as np
from backtracking import BacktrackingSolver
   # Demander A l'utilisateur de saisir le nom du fichier
nom_fichier = input("Entrez le nom du fichier contenant la grille de Sudoku : ")
# Lire le contenu du fichier
grille = []
with open(nom_fichier, 'r') as file:
     
    for line in file:
        
        line = line.strip()  # Supprimer les espaces et les sauts de ligne en debut et fin de ligne
        line = line.replace("_", "0")  # Remplacer les tirets par des 0
        line = [int(num) for num in line];
        grille.append(line) 

# Afficher la gille initiale
matrice =np.array([[line[i] for line in grille] for i in range(len(grille[0]))])

print("La grille initiale est :")

print(matrice)
        
solver = BacktrackingSolver(grille)
solution = solver.resoudre()
print("la grille resolue est:")

if solution is not None:
    # Afficher la grille resolue
    for line in solution:
        line=np.array(line)
        print(line)

else:
    print("Pas de solution trouvee pour cette grille de Sudoku.")
