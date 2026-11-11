##!/usr/bin/python
#-*- coding: UTF-8  -*-

try:
	from model.maillonDijkstra import *
except:
	from maillonDijkstra import *


class Arbre:
	def __init__(self):
		self.__racine=None
		
	### Setteur
	def setRacine(self,pRacine):
		self.__racine=pRacine
	
	### Guetteur
	def getRacine(self):
		return self.__racine
	
	### Initialisation
	def rafraichie(self):
		self.__racine=None
	
	### Recherche dans l'arbre
	def chercherNom(self,pNom):
		if self.__racine.getNom()==pNom:
			return True
		else:
			return self.chercherNomArbre(pNom,self.__racine)
	def chercherNomArbre(self,pNom,maillon):
		if maillon.getNom()==pNom:
			return True
		elif  len(maillon.getSuivants())==0:
			return False
		else:
			reponse=False
			for loop in maillon.getSuivants():
				reponse = reponse or self.chercherNomArbre(pNom,loop)
			return reponse
	
	### Ajout
	def ajouterMaillon(self,pMaillonPrecedent,pMaillonInserer):
		if pMaillonPrecedent==None:
			if self.__racine==None:
				self.__racine=pMaillonInserer
			else:
				pass
		else:
			pMaillonPrecedent.ajouteSuivant(pMaillonInserer)
	def ajouterChaine(self,pChaine):
		if self.__racine==None:
			n1=MaillonDijkstra(pChaine[0],0,None)
			self.ajouterMaillon(None,n1)
			for i in range(2,len(pChaine),2):
				n2=MaillonDijkstra(pChaine[i],0,n1)
				self.ajouterMaillon(n1,n2)
				n1=n2
		else:
			self.__ajouteChaineRe(self.getRacine(),pChaine,0)
	def __ajouteChaineRe(self,maillon,pChaine,i):
		if maillon.getNom()==pChaine[i]:
			if len(pChaine)>i+2:
				j=-1
				for loop in range(len(maillon.getSuivants())):
					if maillon.getSuivants()[loop].getNom()==pChaine[i+2]:
						j=loop
				if j>-1:
					self.__ajouteChaineRe(maillon.getSuivants()[j],pChaine,i+2)
				else:
					while(i+2<len(pChaine)):
						m1=MaillonDijkstra(pChaine[i+2],0,maillon)
						self.ajouterMaillon(maillon,m1)
						maillon=m1
						i+=2
	def ajouteListeChaines(self,listes):
		for loop in listes:
			self.ajouterChaine(loop)
	### Affichage console
	def affichageConsole(self):
		self.__hydrateConsole()
		if self.__racine==None:
			print("Arbre vide")
		else:
			self.__affichageConsoleRecu(self.getRacine(),0)
	def __affichageConsoleRecu(self,maillon,val):
		if maillon.getPrecedent()==None:
			print(maillon.getNom()+"\tligne\t"+str(val)+"\tprofondeur\t"+str(maillon.getProfondeur())+
			"\n\t\t\tPrecedent\tracine+\tNombre de feuille\t")
		else:
			print(maillon.getNom()+"\tligne\t"+str(val)+"\tprofondeur\t"+str(maillon.getProfondeur())+
			"\n\tPrecedent\t"+maillon.getPrecedent().getNom()+"\tNombre de feuilles : "+
			str(maillon.getNombreAncetreFeuille())+"\t"+str(maillon.getPositionVericale()))
		if (len(maillon.getSuivants())>0):
			for loop in range(len(maillon.getSuivants())):
				self.__affichageConsoleRecu(maillon.getSuivants()[loop],val+1)
	def __hydrateConsole(self):
		self.hydrateFeuillage()
		self.hydratePositionVerticale()
	### Paramètres de l'arbre
	def calculHauteur(self):
		if self.__racine==None:
			return 0
		else:
			return self.__getHauteurInterne(self.getRacine(),0)
	def __getHauteurInterne(self,maillon,val):
		if len(maillon.getSuivants())==0:
			return val
		else:
			maxi=self.__getHauteurInterne(maillon.getSuivants()[0],val+1)
			ind=0
			for i in range(len(maillon.getSuivants())):
				if maxi<self.__getHauteurInterne(maillon.getSuivants()[i],val+1):
					maxi=self.__getHauteurInterne(maillon.getSuivants()[i],val+1)
					ind=i
			return maxi
	def calculNbrFeuilles(self):
		if self.__racine==None:
			return 0
		return self.__calculNbrFeuillesInterne(self.getRacine())
	def __calculNbrFeuillesInterne(self,maillon):
		if len(maillon.getSuivants())==0:
			return 1
		else:
			reponse=0
			for i in range(len(maillon.getSuivants())):
				reponse+=self.__calculNbrFeuillesInterne(maillon.getSuivants()[i])
			return reponse
	def nbrFeuillesDessous(self,maillon):
		if len(maillon.getSuivants())==0:
			return 0
		return self.__nbrFeuillesDessousInterne(maillon)
	def __nbrFeuillesDessousInterne(self,maillon):
		if len(maillon.getSuivants())==0:
			return 1
		somme=0
		for loop in maillon.getSuivants():
			somme+=self.__nbrFeuillesDessousInterne(loop)
		return somme
	### Hydratation des attributs des maillons
	def hydrateFeuillage(self):
		if self.__racine==None:
			return 0
		else:
			self.__hydrateFeuillageInterne(self.__racine)
	def __hydrateFeuillageInterne(self,maillon):
		maillon.setNombreAncetreFeuille(self.nbrFeuillesDessous(maillon))
		for i in range(len(maillon.getSuivants())):
			self.__hydrateFeuillageInterne(maillon.getSuivants()[i])
	def hydratePositionVerticale(self):
		if self.__racine==None:
			return 0
		else:
			self.__hydratePositionVerticaleInterne(self.__racine)
	def __hydratePositionVerticaleInterne(self,maillon):
		somme=0
		for i in range(len(maillon.getSuivants())):
			valeur=maillon.getPositionVericale()
			if valeur==None:
				valeur=0
			maillon.getSuivants()[i].setPositionVericale(somme+valeur)
			if maillon.getSuivants()[i].getNombreAncetreFeuille()==0:
				somme+=1
			else:
				somme+=maillon.getSuivants()[i].getNombreAncetreFeuille()
		for i in range(len(maillon.getSuivants())):
			self.__hydratePositionVerticaleInterne(maillon.getSuivants()[i])
	def hydrateValeur(self,tabVal):
		if self.__racine==None:
			return 0
		else:
			self.__hydrateValeurInterne(self.__racine,tabVal)
	def __hydrateValeurInterne(self,maillon,tabVal):
		i=0
		while i<len(tabVal) and maillon.getNom()!=tabVal[i][1]:
			i+=1
		if i<len(tabVal):
			maillon.setValeur(tabVal[i][0])
		for i in range(len(maillon.getSuivants())):
			self.__hydrateValeurInterne(maillon.getSuivants()[i],tabVal)
