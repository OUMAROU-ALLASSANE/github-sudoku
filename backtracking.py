class BacktrackingSolver:
    def __init__(self, grille):
        self.grille = grille

    def absentSurLigne(self, k, i):
        for j in range(9):
            if self.grille[i][j] == k:
                return False
        return True

    def absentSurColonne(self, k, j):
        for i in range(9):
            if self.grille[i][j] == k:
                return False
        return True

    def absentSurBloc(self, k, i, j):
        _i = i - (i % 3)
        _j = j - (j % 3)
        for x in range(_i, _i + 3):
            for y in range(_j, _j + 3):
                if self.grille[x][y] == k:
                    return False
        return True

    def estValide(self, position):
       # Si on est à la 82e case (on sort du tableau) 
        if position == 9 * 9:
            return True
       # On récupère les coordonnées de la case 
        i, j = position // 9, position % 9
       # Si la case n'est pas vide, on passe à la suivante (appel récursif) 
        if self.grille[i][j] != 0:
            return self.estValide(position + 1)
        # Sinon, on tente les chiffres de 1 à 9 pour cette case vide
        for k in range(1, 10):
            
            if self.absentSurLigne(k, i) and self.absentSurColonne(k, j) and self.absentSurBloc(k, i, j):
                 # Si le chiffre est valide, on l'assigne à la case
                self.grille[i][j] = k
               # On continue la résolution avec la case suivante (appel récursif) 
                if self.estValide(position + 1):
                    return True
                 # Si l'assignation ne mène pas à une solution, on réinitialise la case
                self.grille[i][j] = 0

        return False

    def resoudre(self):
        if self.estValide(0):
            return self.grille
        else:
            
            return None
         # Si aucun chiffre ne convient, on revient en arrière (backtracking) 
