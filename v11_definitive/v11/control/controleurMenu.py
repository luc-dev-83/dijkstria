#!/usr/bin/python
#-*- coding: UTF-8  -*-

from tkinter import *
from tkinter.filedialog import *
from control.fonctionsGraphe import *
from control.controlMenuDijksta import *
from control.controlChoixNoeuds import *
from vue.presentation import *
from vue.logo import *
from vue.version import *

class ControleurMenu(Menu):
	def __init__(self,parent,model):
		Menu.__init__(self,parent)
		parent.config(menu=self)
		self.parent=parent

		### Menu fichier 
		self.filemenu=Menu(self,tearoff=0)
		self.filemenu.add_command(label="Sauver",command=self.sauverModel)
		self.filemenu.add_command(label="Nouveau",command=self.initModel)
		self.filemenu.add_command(label="Charger",command=self.chargerModel)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Créer PDF",command=self.creerPdf)
		self.filemenu.add_separator()

                #######################################################################
		self.sousmenu = Menu(self.filemenu,tearoff=0)
		self.sousmenu.add_command(label=".jpg",command=self.ExporterJpg)
		self.sousmenu.add_command(label=".bmp",command=self.ExporterBmp)
		self.filemenu.add_cascade(label="Exporter graphe",menu=self.sousmenu)
		self.filemenu.add_separator()
                ######################################################################

		self.filemenu.add_command(label="Quitter",command=parent.destroy)
		self.add_cascade(label="Fichier",menu=self.filemenu)
		### Menu propriété des cercles
		self.menuCercle=Menu(self,tearoff=0)
		self.add_cascade(label="Cercle",menu=self.menuCercle)
				## rayon
		self.menuChangeRyon=Menu(self.menuCercle,tearoff=0)
		self.menuCercle.add_cascade(label="Changer rayon",menu=self.menuChangeRyon)
		self.menuChangeRyon.add_command(label="Augmenter rayon",command=self.agrandir)
		self.menuChangeRyon.add_command(label="Reduire rayon",command=self.reduire)
		self.menuChangeRyon.add_command(label="Rayon initial",command=self.initial)
				### Pas
		self.menuChangePas=Menu(self.menuCercle,tearoff=0)
		self.menuCercle.add_cascade(label="Changer pas",menu=self.menuChangePas)
		self.menuChangePas.add_command(label="Augmenter pas",command=self.agrandirPas)
		self.menuChangePas.add_command(label="Diminuer pas",command=self.reduirePas)
		self.menuChangePas.add_command(label="Pas initial",command=self.initialPas)

		self.menuCercle.add_separator()
				### Nombre de connections
		self.fileNoeuds=Menu(self.menuCercle,tearoff=0)
		self.menuCercle.add_cascade(label="Changer nbr connexions",menu=self.fileNoeuds)
		self.fileNoeuds.add_command(label="+ de connexions",command=self.agrandirNoeud)
		self.fileNoeuds.add_command(label="- de connexions",command=self.reduireNoeud)
		self.fileNoeuds.add_command(label="Initial",command=self.initialNoeud)
		##### Menu de traitement
		self.menuTraitement=Menu(self,tearoff=0)
		self.add_cascade(label="Traitement",menu=self.menuTraitement)
		self.menuTraitement.add_command(label="Annuler traitement",command=self.annulerTraitement)
				### Dijkstra
		self.dijkstra=Menu(self.menuTraitement,tearoff=0)
		self.menuTraitement.add_cascade(label="Dijkstra",menu=self.dijkstra)
		self.dijkstraDetail=Menu(self.dijkstra,tearoff=0)
		self.dijkstra.add_cascade(label="Dijkstra",menu=self.dijkstraDetail)
		self.dijkstraDetail.add_command(label="Avec detail",command=self.plusCourtCheminAvec)
		self.dijkstraDetail.add_command(label="Sans detail",command=self.plusCourtCheminSans)
		
		
		self.dijkstra.add_command(label="Un point de départ",command=self.unPointDeDepart)
		self.dijkstra.add_command(label="changer en arbre",command=self.changerUnArbre)
		
		### Menu à propos
		self.filePropos=Menu(self,tearoff=0)
		self.filePropos.add_command(label="Présentation",command=self.presentation)
		self.filePropos.add_command(label="Logo",command=self.propos)
		self.filePropos.add_command(label="Version",command=self.version)
		self.add_cascade(label="?",menu=self.filePropos)
		self.model=model
### Fonctions menus fichiers
	def initModel(self):
		self.model.init()
	def sauverModel(self):
		self.model.sauver()
	def chargerModel(self):
		self.model.charger()
	def creerPdf(self):
		self.parent.cadreGauche.graphe.postscript(colormode='color',file='image')

	##### fonctions ajoutées ###############
	def ExporterJpg(self):
		self.model.exporterJpg()
	def ExporterBmp(self):
		self.model.exporterBmp()		
	##### fin fonctions ajoutées ###########	

#### Fonctions menus canvas
	def agrandir(self):
		r=self.model.getPas()
		p=self.model.getRayon()
		r2=r*pow(p,1)
		liste=self.model.getListeNoeuds()
		ecarte(r2,liste)
		self.model.setRayon(1)
																				#####
	def reduire(self):
		self.model.setRayon(-1)
	def initial(self):
		self.model.initRayon()
#### Gestion du pas	
	def agrandirPas(self):
		self.model.setPas(1)
	def reduirePas(self):
		self.model.setPas(-1)
	def initialPas(self):
		self.model.initPas()
		
#### Fonctions menus noeud
	def agrandirNoeud(self):
		self.model.setNbrCo(1)
	def reduireNoeud(self):
		self.model.setNbrCo(-1)
	def initialNoeud(self):
		self.model.initNbrCo()
### menu traitement
	def annulerTraitement(self):
		initialiserBrancheNoeud(self.model.getListeNoeuds(),self.model.getListeBranche())
		self.model.setTraitement(0)
		self.model.initTraitement()
### menu Dijkstra
	def plusCourtCheminAvec(self):
		self.model.initTraitement()
		plusCourtCheminDijkstra(self.model)
		noeuds=ControlChoixNoeuds("Nom du point de départ :","Nom du point d'arrivée :",self.model,2)
		self.model.setTraitement(1)
	def plusCourtCheminSans(self):
		self.model.initTraitement()
		plusCourtCheminDijkstra(self.model)
		noeuds=ControlChoixNoeuds("Nom du point de départ :","Nom du point d'arrivée :",self.model,2)
		self.model.setTraitement(2)
	def unPointDeDepart(self):
		self.model.initTraitement()
		plusCourtCheminDijkstra(self.model)
		noeuds=ControlChoixNoeuds("Nom du point de départ :","",self.model,1)
		self.model.setTraitement(3)
	def changerUnArbre(self):
		self.model.initTraitement()
		plusCourtCheminDijkstra(self.model)
		noeuds=ControlChoixNoeuds("Nom du point de départ :","",self.model,1)
		self.model.setTraitement(4)
### menu explication
	def presentation(self):
		noeuds=Presentation()
	def propos(self):
		noeuds=Logo()
	def version(self):
		noeuds=Version()

