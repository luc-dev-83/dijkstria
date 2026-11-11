#!/usr/bin/python
#-*- coding: UTF-8  -*-

from model.observable import *
from model.noeud import *
from model.branche import *
from model.fichier import *
from model.arbre import *
from model.exportationGraphe import *



class Modele(Observable):
	def __init__(self):
		### Taille des cadres
		Observable.__init__(self)
		self.largeurEcran=0
		self.hauteurEcran=0
		self.largeurCadreGauche=0
		self.hauteurCadreDroit=0
		self.hauteurCadreGauche=0
		
		### Données relatives au graphe
		self.listeNoeuds=[]
		self.listeBranche=[]
		self.listeDeuxNoeuds=[-1,-1]
		self.positionClickDroit=-1
		
		### Constante : représentation et connexions possibles
		self.rayon=15
		self.pas=2
		self.nbrCo=6
		
		### Mode de traitement
		self.traitement=0
		self.hauteurCadreDroitBas=0
		self.largeurCadreDroit=0
		self.listeNoeudsTraitement=["",""]
		self.nbrTours=0
		self.tableauTravail=[]
		self.reponse=(0,"")
		self.noeudNonVisite=""
		
		### label gauche bas
		self.label=""
		self.arbre=Arbre()
### Fonctions de gestion de la taille des cadres
	def setEcran(self,x,y,z):
		self.largeurEcran=int(x)
		self.hauteurEcran=int(y)
		self.setLargeurCadreGauche(int(z))
		self.setHauteurCadreGauche(int(4*y/5))
		self.setHauteurCadreDroit(int(y/5))
		self.actualise()
	def setEcranDroit(self,val):
		self.setHauteurCadreDroit(int(self.hauteurCadreDroit+val))
		self.actualise()
	def setEcranGauche(self,val):
		self.setHauteurCadreGauche(int(self.hauteurCadreGauche+val))
		self.actualise()
	def setEcranHorizon(self,val):
		self.setLargeurCadreGauche(int(self.largeurCadreGauche+val))
		self.actualise()

	def setLargeurEcran(self,val):
		self.largeurEcran=int(val)
	def setHauteurEcran(self,val):
		self.hauteurEcran=int(val)
	def setLargeurCadreGauche(self,val):
		self.largeurCadreGauche=int(val)
		self.largeurCadreDroit=self.largeurEcran-int(val)-20
	def setHauteurCadreDroit(self,val):
		self.hauteurCadreDroit=int(val)
		self.hauteurCadreDroitBas=self.hauteurEcran-int(val)-20
		
	def setHauteurCadreGauche(self,val):
		self.hauteurCadreGauche=int(val)

	def setRayonSauv(self,val):
		self.rayon=int(val)
	def setPasSauv(self,val):
		self.pas=int(val)
	def setNbrCoSauv(self,val):
		self.nbrCo=int(val)		
	def setListeDeuxNoeuds(self,val1,val2):
		self.listeDeuxNoeuds[0]=val1
		self.listeDeuxNoeuds[1]=val2	
	def setPositionClickDroit(self,val):
		self.positionClickDroit=val
	def setReponse(self,obj):
		self.reponse=obj
	### set de traitement
	def setTraitement(self,val):
		self.traitement=val
		self.actualise()
	def setLlisteNoeudsTraitement(self,obj):
		self.listeNoeudsTraitement=obj
		self.actualise()
	def setNbrTours(self,val):
		self.nbrTours=val
		self.actualise()
	def augNbrTours(self):
		self.nbrTours+=1
		self.actualise()
	def setTableauTravail(self,obj):
		self.tableauTravail=obj
	def ajouTableauTravail(self,obj):
		self.tableauTravail.append(obj)
		self.actualise()
	def setNoeudNonVisite(self,val):
		self.noeudNonVisite=val
#### Fonctions chargement sauvegarde
	def init(self):						### initialisation des données 
		self.listeNoeuds=[]
		self.listeBranche=[]
		self.listeDeuxNoeuds=[-1,-1]
		self.rayon=15
		self.pas=5
		self.nbrCo=6
		self.initTraitement()
		self.label=""
		self.arbre.rafraichie()
		self.actualise()
	def sauver(self):
		sauverModel(self)
	def charger(self):
		self.init()
		self.initTraitement()
		chargeModel(self)
	
	def initTraitement(self):				### fonctions d'initialisation du mode traitement (cadre droit bas)
		self.traitement=0
		self.label=""
		self.arbre.rafraichie()
		self.noeudNonVisite=""
		self.initTableauTravail()
		self.nbrTours=0
		del(self.listeNoeudsTraitement)
		self.listeNoeudsTraitement=["",""]
		for noeud in self.listeNoeuds:
			noeud.setCouleur('black')
		for branche in self.listeBranche:
			branche.setCouleur('black')
		self.actualise()
	def initTableauTravail(self):
		while (len(self.tableauTravail))>0:
			if type(self.tableauTravail)==str:
				self.tableauTravail=[]
			else:
				del(self.tableauTravail[len(self.tableauTravail)-1])
	def initInformations(self):				### cadre informations diverses
		pass

#### Guetteur
	def getListeNoeuds(self):
		return self.listeNoeuds
	def getListeBranche(self):
		return self.listeBranche
	def getRayon(self):
		return self.rayon
	def getNbrCo(self):
		return self.nbrCo
	def getListeDeuxModeles(self):
		return self.listeDeuxNoeuds
	def getLargeurEcran(self):
		return self.largeurEcran
	def getHauteurEcran(self):
		return self.hauteurEcran
	def getPas(self):
		return self.pas
	def getLargeurCadreGauche(self):
		return self.largeurCadreGauche
	def getLargeurCadreDroit(self):
		return self.largeurCadreDroit
	def getHauteurCadreDroit(self):
		return self.hauteurCadreDroit
	def getHauteurCadreGauche(self):
		return self.hauteurCadreGauche		
	def getPositionClickDroit(self):
		return self.positionClickDroit
		
	### get de traitement
	def getTraitement(self):
		return self.traitement
	def getLargeurCadreDroit(self):
		return self.largeurCadreDroit
	def getHauteurCadreDroitBas(self):
		return self.hauteurCadreDroitBas
	def getListeNoeudsTraitement(self):
		return self.listeNoeudsTraitement
	def getNbrTours(self):
		return self.nbrTours
	def getTableauTravail(self):
		return self.tableauTravail
	def getReponse(self):
		return self.reponse				# objet de type liste : distance ou 0 et chemin ou texte
	def getNoeudNonVisite(self):
		return self.noeudNonVisite
	
	def getLabel(self):
		return self.label
#### changement particulier des valeurs de certains attributs
	def initRayon(self):
		self.rayon=15
		self.actualise()
	def setRayon(self,val):
		self.rayon=self.rayon*pow(self.pas,val)
		self.actualise()
	def initPas(self):
		self.pas=2
	def setPas(self,val):
		self.pas+=val
	def setNbrCo(self,val):
		self.nbrCo+=val
	def initNbrCo(self):
		self.nbrCo=6
	def delTableauTravail(self,val):
		while (len(self.tableauTravail)>val):
			del(self.tableauTravail[len(self.tableauTravail)-1])

#### Noeud
	def ajouterNoeud(self,obj):
		self.listeNoeuds.append(Noeud(obj,self.nbrCo))
		self.actualise()
	def repositionneUnNoeud(self,px,py,numNoeud):
		(self.listeNoeuds[numNoeud]).setPosition(px,py)
		self.actualise()
	def changeStyleNoeud(self,numNo,val):
		if val==0:
			if numNo==self.listeDeuxNoeuds[1]:
				self.listeDeuxNoeuds[1]=-1
			if numNo==self.listeDeuxNoeuds[0]:
				self.listeDeuxNoeuds[0]=self.listeDeuxNoeuds[1]
				self.listeDeuxNoeuds[1]=-1
		if val==1:
			if self.listeDeuxNoeuds[1]==-1 and self.listeDeuxNoeuds[0]==-1:
				self.listeDeuxNoeuds[0]=numNo
			elif self.listeDeuxNoeuds[1]==-1:
				self.listeDeuxNoeuds[1]=numNo
			else:
				(self.listeNoeuds[self.listeDeuxNoeuds[0]]).setStyle(0)
				self.listeDeuxNoeuds[0]=self.listeDeuxNoeuds[1]
				self.listeDeuxNoeuds[1]=numNo
		if val==2:									### Initialisation du style
			if self.listeDeuxNoeuds[0]!=-1:
				(self.listeNoeuds[self.listeDeuxNoeuds[0]]).setStyle(0)
				self.listeDeuxNoeuds[0]=-1
			if self.listeDeuxNoeuds[1]!=-1:
				(self.listeNoeuds[self.listeDeuxNoeuds[1]]).setStyle(0)
				self.listeDeuxNoeuds[1]=-1
			self.actualise()
			return 0
		(self.listeNoeuds[numNo]).setStyle(val)
		self.actualise()
	def supprimeNoeud(self,NumNoeud):
		self.changeStyleNoeud(NumNoeud,0)
		if self.listeDeuxNoeuds[0]>NumNoeud:
			self.listeDeuxNoeuds[0]-=1
		for i in range(NumNoeud,len(self.listeNoeuds)-1):
			self.listeNoeuds[i]=self.listeNoeuds[i+1]
		for branche in self.listeBranche:
			if branche.getNumA()>NumNoeud-1:
				branche.setNumA(branche.getNumA()-1)
			if branche.getNumB()>NumNoeud-1:
				branche.setNumB(branche.getNumB()-1)
		del(self.listeNoeuds[len(self.listeNoeuds)-1])
		self.actualise()
		
	### Gestion des styles des petits carrés
	def changeStyleCarre(self,numNo,numCar,val):
		noeud=self.listeNoeuds[numNo]
		if val==0:
			noeud.setNumCarre(numCar,val)
			self.actualise()
		if val==1:
			nbrCo=noeud.getNbrConnection()
			for k in range(nbrCo):
				styleC=noeud.getNumCarre(k)
				if k!=numCar and styleC==1:
					self.changeStyleCarre(numNo,k,0)
			noeud.setNumCarre(numCar,val)
			self.actualise()
		if val==2:
			noeud.setNumCarre(numCar,val)
			self.actualise()
		if val==3:										### forcer le passage à l'état 0
			noeud.setNumCarre(numCar,0)

### Branche
	def ajouteBranche(self,obj):									## (noeud1,ind1,noeud2,ind2))
		self.listeBranche.append(Branche(obj))
		self.changeStyleCarre(obj[0],obj[1],2)
		self.changeStyleCarre(obj[2],obj[3],2)
		self.actualise()
	def supprimeBranche(self,num):
		branche=(self.listeBranche[num]).getAttributs()
		self.changeStyleCarre(branche[0],branche[1],3)
		self.changeStyleCarre(branche[2],branche[3],3)
		for i in range(num,len(self.listeBranche)-1):
			self.listeBranche[i]=self.listeBranche[i+1]
		del(self.listeBranche[len(self.listeBranche)-1])
		self.actualise()

	def supprimePlusieursBranche(self,listeBr,NumNoeud):
		while len(listeBr)>0:
			self.supprimeBranche(listeBr[len(listeBr)-1])
			del(listeBr[len(listeBr)-1])
		self.supprimeNoeud(NumNoeud)
### Arbre
	def getArbre(self):
		return self.arbre
	def setArbre(self,pArbre):
		self.arbre=pArbre
	def construireArbre(self):
		self.arbre.ajouteListeChaines([self.reponse[k][1] for k in range(1,len(self.reponse))])
		self.arbre.hydrateFeuillage()
		self.arbre.hydratePositionVerticale()
		tabVal=[]
		for loop in self.getReponse():
			tabVal.append((loop[0],loop[1][len(loop[1])-1]))
		self.arbre.hydrateValeur(tabVal)
		self.actualise()
	def initArbre(self,pNom):
		self.arbre.setRacine(MaillonDijkstra(pNom,0,None))
		## Change style du noeud
		self.actualise()
	def completeArbre(self):
		nom=self.arbre.getRacine().getNom()
		
		self.actualise()

### Bibliotèque PIL
	def exporterJpg(self):
		ExporterJpg(self)
	def exporterBmp(self):
		ExporterBmp(self)

