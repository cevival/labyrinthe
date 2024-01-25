import random
import csv

class Labyrinthe :
    # constructeur
    def __init__(self, sizeX, sizeY, filesName):
        """sizeX, sizeY désignent la taille du labyrinthe sur l'axe (x,y)"""
        self.sizeX = sizeX
        self.sizeY = sizeY
        #attention création d'une matrice en Y X
        self.matrice = [ [0]* self.sizeX for _ in range(self.sizeY) ]
        self.fn = filesName
        self.map = []

    def affiche(self):
        """Sortie console du labyrinthe"""
        for j in range(self.sizeY):
            for i in range(self.sizeX):
                # rappel: matrice en Y,X
                print(self.matrice[j][i], end = "")
            print()

    def readFiles(self):
        with open(self.fn, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                rowListe = [int(cell)for cell in row]
                self.map.append(rowListe)
    
    def achiffeMap(self):
        for row in self.map: 
            print(row)

    def get_matrice(self):
        """renvoie la matrice associée au labyrinthe"""
        return self.matrice
    
    def getXY(self, i,j):
        """Renvoie la case (i,j) du labyrinthe sur l'axe (x,y)"""
        return self.matrice[j][i]

    def setXY(self, i,j,v):
        """Modifie par v la case (i,j) sur l'axe (x,y)"""
        self.matrice[j][i] = v
    
    def getSize(self):
        """Renvoie la taille (x,y) du labyrinthe"""
        return (self.sizeX, self.sizeY)
    
    def détruire_mur(self, i,j):
        """Détruit un mur du labyrinthe en (i,j) sur l'axe (x,y)"""
        self.matrice[j][i]=0


laby = Labyrinthe(12,5,'laby-01.csv')
laby.setXY(5,2,1)
print(laby.getSize())
laby.affiche()

print(laby.get_matrice())
print(laby.getXY(5,2))


l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = [11,12,13,14,15]
lst = []
lst.append(l1)
lst.append(l2)
lst.append(l3)
print(lst)

print(lst[2][1])
laby.readFiles()
laby.achiffeMap()