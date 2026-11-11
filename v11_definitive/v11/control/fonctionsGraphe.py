from math import *

def noeudExiste(xEvt,yEvt,listeNoeuds,r):							### Vérifie si un noeud est près des coordonnées
	for loop in listeNoeuds:
		if (loop.x-xEvt)*(loop.x-xEvt)+(loop.y-yEvt)*(loop.y-yEvt)<r*r:
			return True
	return False

def lettreSuivantes(listeNoeuds):									### Enumération de l'alphabet
	i=65
	while lettreExiste(listeNoeuds,i):
		i+=1
	return i
def lettreExiste(listeNoeuds,val):
	for loop in listeNoeuds:
		if loop.nom==chr(val):
			return True
	return False

def numNoeud(xEvt,yEvt,listeNoeuds,r):								### Retourne la valeur de l'indice du noeud dans le tableau
	val=0															### -2 en cas d'échec
	for loop in listeNoeuds:
		if (loop.x-xEvt)*(loop.x-xEvt)+(loop.y-yEvt)*(loop.y-yEvt)<r*r:
			return val
		val+=1
	return -2
def distance(ptA,ptB,r):											### Retourne vrai si les boules sont proches
	return pow(ptA[0]-ptB[0],2)+pow(ptA[1]-ptB[1],2)<4*r*r

def collision(numNoeud,px,py,listeNoeuds,rayon):					### Recherche si un noeud entre en collision
	for loop in listeNoeuds:
		if listeNoeuds[numNoeud]!=loop:
			if distance((px,py),loop.getPosition(),rayon):
				return True											### Collision
	return False

def numCarre(px,py,coords,nb,r):									### Cherche le numero du carré lors d'un click de souris
	for i in range(nb):
		x=coords[0]+r*cos(2*pi*i/nb)
		y=coords[1]+r*sin(2*pi*i/nb)
		if (x-r/5<px and px<x+r/5):
			if (y-r/5<py and py<y+r/5):
				return i
	return -2

def rechercheIndice(noeud):											### Cherche l'indice du carré de style 1
	maxi=noeud.getNbrConnection()
	for k in range(maxi):
		if noeud.getNumCarre(k)==1:
			return k
	return -2
def longueur(x,y):
	return sqrt(x*x+y*y)

def ecarte(r2,liste):								### Ecarte tous les noeuds à une distance de 1.2r
	compteur=0
	xa=liste[0].getX()
	ya=liste[0].getY()
	for i in range(1,len(liste)):
		xc=liste[i].getX()
		yc=liste[i].getY()
		for j in range (0,i):
			xb=liste[j].getX()
			yb=liste[j].getY()
			while distance((xc,yc),(xb,yb),1.2*r2):
				xc=xc+r2*(xc-xa)/longueur(xa,ya)
				yc=yc+r2*(xc-xa)/longueur(xa,ya)
				liste[i].setPosition(xc,yc)
