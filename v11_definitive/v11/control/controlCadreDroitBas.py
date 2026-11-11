#!/usr/bin/python
#-*- coding: UTF-8  -*-
from control.fonctionsGraphe import *
from math import *

class ControlCadreDroitBas:
	def __init__(self,vue,model):
		self.model=model
		self.vue=vue
		self.vue.bind("<Button-1>",self.click1)
		self.vue.bind("<Button-3>",self.click3)
	def click1(self,evt):
		if self.model.getTraitement()==0:
			pass
		elif self.model.getTraitement() in (1,2,3,4):									####getTraitement
			if self.model.getNbrTours()==0:
				self.constructionTableau()
				self.model.augNbrTours()
			else:
				if self.model.getNbrTours()%2==0:
					self.miseAjourPair(self.model.getNbrTours())
				else:
					self.miseAjourImPair(self.model.getNbrTours())
				if self.model.getNbrTours()<2*len(self.model.getTableauTravail())+2:
					self.model.augNbrTours()
		elif self.model.getTraitement()==5:
			pass
		elif self.model.getTraitement()==6:
			if self.model.getNbrTours()==0:
				self.model.setTableauTravail(self.model.getListeNoeudsTraitement()[0])
				self.model.initArbre(self.model.getListeNoeudsTraitement()[0])
				self.model.getListeNoeudsTraitement()[0]
				self.model.setNbrTours(1)
			if self.model.getNbrTours()>0:
				self.model.setNbrTours(self.model.getNbrTours()+1)
				self.model.completeArbre()
				
				
				
	def constructionTableau(self):
		tabTrav=self.model.getTableauTravail()
		if self.model.getNbrTours()==0:
			listeNoeuds=self.model.getListeNoeuds()
			nbrNoeuds=len(listeNoeuds)
			listeDonnees=self.model.getListeNoeudsTraitement()
			listeBranche=self.model.getListeBranche()
			if len(tabTrav)==0:
				l0=[]
				for noeud in listeNoeuds:
					if noeud.getNom()==str(listeDonnees[0]):
						l0.append((0,noeud.getNom()))
						noeud.setCouleur('green')
					else:
						l0.append(('X',""))
				self.model.ajouTableauTravail(l0)
			valMin=1
			while valMin!=-1:
				nouvelleLigne=[]
				ligne=self.model.getTableauTravail()[len(self.model.getTableauTravail())-1]
				valMin=-1
				### Recherche du pivot
				for i in range(nbrNoeuds):
					if ligne[i][0]=='X' or ligne[i][0]=='+':
						pass
					elif valMin==-1 or valMin>ligne[i][0]:
						indiceMin=i
						valMin=float(ligne[i][0])
				if valMin!=-1:
				### Fabrication nouvelle ligne
					for i in range(nbrNoeuds):
						if i==indiceMin or ligne[i][0]=='+':
							nouvelleLigne.append(('+',""))
						else:					
							val=float(self.distanceNoeud(i,indiceMin))
							if val==-1:
								nouvelleLigne.append(ligne[i])
							elif ligne[i][0]=='X':
								nouvelleLigne.append((val+valMin,ligne[indiceMin][1]+"-"+listeNoeuds[i].getNom()))
							elif val+valMin<(ligne[i][0]):
								nouvelleLigne.append((val+valMin,ligne[indiceMin][1]+"-"+listeNoeuds[i].getNom()))
							else:
								nouvelleLigne.append(ligne[i])
					self.model.ajouTableauTravail(nouvelleLigne)
			# Recherche de la solution										# listeDonnees[0]   noeud de depart
			if self.model.getTraitement() in (1,2):							###  getTraitement
				i=0
				for noeud in listeNoeuds:
					if str(listeDonnees[1])==noeud.getNom():
						indice=i
					i+=1
				tabTrav=self.model.getTableauTravail()
				i=0
				for ligne in tabTrav:
					if (ligne[indice])[0]=="+":
						if i==0:
							self.model.setReponse((0,"arrive"))
						elif (pivot)[0]!="+":
							self.model.setReponse(pivot)
							if self.model.getTraitement() in (1,2):				#### Destruction des lignes inutiles
								self.model.delTableauTravail(i)
					i+=1
					pivot=ligne[indice]
				if ((tabTrav[len(tabTrav)-1])[indice])[0]!='X' and ((tabTrav[len(tabTrav)-1])[indice])[0]!='+':
					self.model.setReponse((tabTrav[len(tabTrav)-1])[indice])
				if ((tabTrav[len(tabTrav)-1])[indice])[0]=="X":
					self.model.setReponse((0,"aucun chemin possible"))
					
			#########################################################
			
			#############   Traitement 3 et 4 :              ########
			
			#############  Création de la liste reponse 	 ########
		
			#########################################################
			
			
			if self.model.getTraitement() in (3,4):
				i=0
				for noeud in listeNoeuds:
					if str(listeDonnees[0])==noeud.getNom():
						indice=i
					i+=1
				tabTrav=self.model.getTableauTravail()
				i=0
				rep=[(0,"Liste des destinations possibles")]
				for i in range(nbrNoeuds):
					for j in range(len(tabTrav)):
						if ((tabTrav[j])[i])[0]=='X':							### maillon lignes j noeuds i
							pass
						elif j>0:	
							if ((tabTrav[j-1])[i])[0]!="+" and ((tabTrav[j])[i])[0]=="+":
								rep.append((((tabTrav[j-1])[i])[0],((tabTrav[j-1])[i])[1]))
				self.model.setReponse(rep)

			#########################################################
			
			#############   Traitement 3 et 4 :              ########
			
			#############  Noeuds non visités			 	 ########
		
			#########################################################				
			rep=""
			ligne=(self.model.getTableauTravail())[len(self.model.getTableauTravail())-1]
			for i in range(len(self.model.getListeNoeuds())):
				if ligne[i][0]=="X":
					if rep=="":
						rep=((self.model.getListeNoeuds())[i]).getNom()
					else:
						rep=rep+"-"+((self.model.getListeNoeuds())[i]).getNom()
			self.model.setNoeudNonVisite(rep)

			#########################################################
			
			#############   Traitement  4 :       	   	       ######
			
			#############  Construction de l'arbre  		 	 ####
		
			#########################################################	
			
			if self.model.getTraitement()==4:
				self.model.construireArbre()
				
				
				
	def distanceNoeud(self,i,indiceMin):
		valMin=-1
		for branche in self.model.getListeBranche():
			if branche.getNumA()==i:
				if branche.getNumB()==indiceMin:
					if valMin==-1:
						valMin=branche.getValeur()						
					elif branche.getValeur()<valMin:
						valMin=branche.getValeur()
		return valMin
	def click3(self,event):
		self.model.initTraitement()
		self.model.actualise()
		
		
	def miseAjourPair(self,indice):
		tabTrav=self.model.getTableauTravail()
		noeuds=self.model.getListeNoeuds()
		if indice==0:
			for noeud in noeuds:
				noeud.setCouleur('black')
			ligne=tabTrav[0]
			i=0
			for maillon in ligne:
				if maillon[0]==0:
					noeuds[i].setCouleur('red')
				i+=1
			self.model.actualise()
		else:
			if indice<2*len(tabTrav):
				lignePrec=tabTrav[int(indice/2-1)]
				ligne=tabTrav[int(indice/2)]
				self.transforme(lignePrec,'green')
				self.transforme(ligne,'blue')
				
				ligne=self.model.getTableauTravail()[int((indice)//2)]
				valMin=0
				chaine=""
				for maillon in ligne:
					if maillon[0]=='X' or maillon[0]=='+':
						pass
					elif valMin==0:
						valMin=maillon[0]
						chaine=maillon[1]
					elif maillon[0]<valMin:
						valMin=maillon[0]
						chaine=maillon[1]
				self.transforme(((0,chaine),(0,chaine)),'red')
				
	def miseAjourImPair(self,indice):
		
		try:
			if len(self.model.getTableauTravail())>int((indice-1)//2)+1:
				ligne=self.model.getTableauTravail()[int((indice-1)//2)]
				valMin=0
				chaine=""
				for maillon in ligne:
					if maillon[0]=='X' or maillon[0]=='+':
						pass
					elif valMin==0:
						valMin=maillon[0]
						chaine=maillon[1]
					elif maillon[0]<valMin:
						valMin=maillon[0]
						chaine=maillon[1]
				self.transforme(((0,chaine),(0,chaine)),'red')
		except:
			pass
	def transforme(self,ligne,couleur):
		for maillon in ligne:
			self.rechercheChemin(maillon[1],couleur)
	def rechercheChemin(self,chaine,couleur):
		listeNoms=chaine.split("-")
		noeuds=self.model.getListeNoeuds()
		for noeud in noeuds:
			if noeud.getNom() in listeNoms:
				noeud.setCouleur(couleur)
		for indice in range(len(listeNoms)-1):
			num=self.valBrancheExiste(listeNoms[indice],listeNoms[indice+1])
			if num>-1:
				(self.model.getListeBranche())[num].setCouleur(couleur)
	def valBrancheExiste(self,nomA,nomB):
		listeBranche=self.model.getListeBranche()
		listeNoeuds=self.model.getListeNoeuds()
		rep=-2
		for i in range(len(listeBranche)):
			if listeNoeuds[listeBranche[i].getNumB()].getNom()==nomA:
				if listeNoeuds[listeBranche[i].getNumA()].getNom()==nomB:
					if rep==-2:
						rep=i
					elif listeBranche[i].getValeur()<listeBranche[rep].getValeur():
						rep=i
		return rep
			
		

