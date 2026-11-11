#!/usr/bin/python
#-*- coding: UTF-8  -*-
from model.arbre import *


print("\t\tEtape 1 : création de l'arbre et ajout manuel de maillon")
A=Arbre()
n1=MaillonDijkstra("A",0,None)
print(A.getRacine())
A.ajouterMaillon(None,n1)
print(A.getRacine().getNom())
n2=MaillonDijkstra("B",4,n1)
n3=MaillonDijkstra("C",8,n1)
n4=MaillonDijkstra("D",12,n2)
n5=MaillonDijkstra("E",16,n4)
n6=MaillonDijkstra("F",12,n4)
n7=MaillonDijkstra("G",12,n4)
A.ajouterMaillon(n1,n2)
A.ajouterMaillon(n1,n3)
A.ajouterMaillon(n2,n4)
print("\nFeuilles dessous")
print(A.nbrFeuillesDessous(n2))
print("\n")
A.ajouterMaillon(n4,n5)
A.ajouterMaillon(n4,n6)
A.ajouterMaillon(n4,n7)

print("\nFeuilles dessous")
print(A.nbrFeuillesDessous(n2))
print("\n")

print(A.getRacine().getSuivants()[0].getNom())
print(A.getRacine().getSuivants()[1].getNom())
print(A.getRacine().getSuivants()[0].getSuivants()[0].getNom())
print(A.getRacine().getSuivants()[0].getSuivants()[0].getSuivants()[0].getNom())
print(A.getRacine().getSuivants()[0].getSuivants()[0].getSuivants()[1].getNom())
print(A.getRacine().getSuivants()[0].getSuivants()[0].getSuivants()[2].getNom())	
print(A.chercherNom("A"))
print(A.chercherNom("C"))
print(A.chercherNom("F"))
print(A.chercherNom("G"))
print(A.chercherNom("z"))
A.affichageConsole()
A.rafraichie()
print(A.getRacine())
try:
	print(A.getRacine().getSuivants()[0].getNom())
except:
	print("probleme")
print("\n\t\tEtape 2 : création de l'arbre et ajout d'une chaine 'A-B-E'")
chaine="A-B-E-F-K-M"
A.ajouterChaine(chaine)
A.affichageConsole()	
chaine2="A-B-C-D"
print("\nInsertion")
A.ajouterChaine(chaine2)
print("\nDeuxième afichage")
A.affichageConsole()
chaine3="A-B-C-O-R"
print("\nInsertion")
A.ajouterChaine(chaine3)
print("\nTroisième afichage")
A.affichageConsole()
chaine4="A-0-1-2-3"
print("\nInsertion")
A.ajouterChaine(chaine4)
print("\nQuatrième afichage")
A.affichageConsole()	
print("\n\t\tEtape 3 : liste de chaines")
A.rafraichie()
listesChaines=[chaine,chaine2,chaine3,chaine4]
A.ajouteListeChaines(listesChaines)
A.affichageConsole()
print("\nHauteur de l'arbre :  "+str(A.calculHauteur()))
print("\nNombre de feuilles :  "+str(A.calculNbrFeuilles()))


A.rafraichie()
listesChaines2=[
"A-B-C-D","A-B-C-E","A-B-C-F",
"A-B-G-A","A-B-G-B",
"A-C-A","A-C-B",
"A-D-A","A-D-B"
]
A.ajouteListeChaines(listesChaines2)
A.affichageConsole()
print("\nHauteur de l'arbre :  "+str(A.calculHauteur()))
print("\nNombre de feuilles :  "+str(A.calculNbrFeuilles()))
A.rafraichie()

A.rafraichie()
listesChaines2=[
"B","B-C","B-C-N-F-D",
"B-C-N-F-G","B-C-N-F-G-H",
"B-C-N-F-G-H-J","B-C-N-F-G-H-J-K",
"B-C-N-F-G-H-M","B-C-N-F","B-C-N","E-I"
]
A.ajouteListeChaines(listesChaines2)
A.affichageConsole()
print("\nHauteur de l'arbre :  "+str(A.calculHauteur()))
print("\nNombre de feuilles :  "+str(A.calculNbrFeuilles()))
A.rafraichie()

listesChaines4=[
"A-B-C-D","A-B-C-E","A-B-F",
"A-G-H-I","A-G-H-J-L",
"A-G-H-K"
]
A.ajouteListeChaines(listesChaines4)
A.affichageConsole()
print("\nHauteur de l'arbre :  "+str(A.calculHauteur()))
print("\nNombre de feuilles :  "+str(A.calculNbrFeuilles()))

A.rafraichie()

listesChaines5=[
"A-B-C-G","A-B-D","A-B-E-H-J",
"A-B-E-I","A-B-F-K-L",
]
A.ajouteListeChaines(listesChaines5)
A.affichageConsole()
print("\nHauteur de l'arbre :  "+str(A.calculHauteur()))
print("\nNombre de feuilles :  "+str(A.calculNbrFeuilles()))

