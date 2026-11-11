#!/usr/bin/python
#-*- coding: UTF-8  -*-
from control.fonctionsGraphe import *
from math import *

class ControlCadreGaucheHaut:
	def __init__(self,vue,model):
		self.model=model
		self.parent=vue
		self.vue=vue.graphe
		self.vue.bind("<Button-1>",self.click1)
		self.vue.bind("<Button-3>",self.click3)
		self.vue.bind("<B1-Motion>",self.click1Mvt)
		self.vue.bind("<B3-Motion>",self.click3Mvt)
		self.vue.bind("<ButtonRelease-3>",self.relache3)
	def click1(self,evt):
		if self.model.getTraitement()==0:
			liste=self.model.getListeNoeuds()
			rayon=self.model.getRayon()
			if (noeudExiste(evt.x,evt.y,liste,2*rayon)):
				numNo=numNoeud(evt.x,evt.y,liste,1.2*rayon)
				if numNo>-1:
					noeud=liste[numNo]
					if noeud.getStyle()==1:
						numCar=numCarre(evt.x,evt.y,noeud.getPosition(),noeud.getNbrConnection(),rayon)
						if numCar==-2:
							self.model.changeStyleNoeud(numNo,0)
						else:	
							if noeud.getNumCarre(numCar)==1:
								self.model.changeStyleCarre(numNo,numCar,0)
							elif noeud.getNumCarre(numCar)==0:
								self.model.changeStyleCarre(numNo,numCar,1)
								
					elif noeud.getStyle()==0:
						self.model.changeStyleNoeud(numNo,1)
			else:
				if self.parent.getSaisie()!="":
					self.model.ajouterNoeud((evt.x,evt.y,self.parent.getSaisie()))
				else:
					self.model.ajouterNoeud((evt.x,evt.y,chr(lettreSuivantes(liste))))
	def click3(self,evt):
		if self.model.getTraitement()==0:
			liste=self.model.getListeNoeuds()
			noeud1=(self.model.getListeDeuxModeles())[1]
			noeud2=(self.model.getListeDeuxModeles())[0]
			if noeud1!=-1:										## Si deux maillons sont en rouge : création d'une branche
				if noeud2!=-1:
					ind1=rechercheIndice(liste[noeud1])
					ind2=rechercheIndice(liste[noeud2])
					if (ind1!=-2 and ind2!=-2):
						if self.parent.getSaisie()!="":
							self.model.ajouteBranche((noeud1,ind1,noeud2,ind2,self.parent.getSaisie()))
						else:
							self.model.ajouteBranche((noeud1,ind1,noeud2,ind2,1))
						return 0
			i=0
			r=self.model.getRayon()
			for loop in self.model.getListeBranche():
				parametre=loop.getAttributs()
				liste=self.model.getListeNoeuds()
				noeud1=liste[parametre[0]]
				noeud2=liste[parametre[2]]
				x1=noeud1.getX()+r*cos(2*pi*parametre[1]/noeud1.getNbrConnection())
				y1=noeud1.getY()+r*sin(2*pi*parametre[1]/noeud1.getNbrConnection())
				x2=noeud2.getX()+r*cos(2*pi*parametre[3]/noeud2.getNbrConnection())
				y2=noeud2.getY()+r*sin(2*pi*parametre[3]/noeud2.getNbrConnection())
				if (y1<evt.y and evt.y<y2) or (y2<evt.y and evt.y<y1):
					if (x1<evt.x and evt.x<x2) or (x2<evt.x and evt.x<x1):
						self.model.supprimeBranche(i)
				i+=1
			i=0
			if (noeudExiste(evt.x,evt.y,liste,r)):
				numNo=numNoeud(evt.x,evt.y,liste,1.2*r)
				if numNo>-1:
					branches=self.model.getListeBranche()
					listeBr=[]
					for branche in branches:
						if (branche.getAttributs())[0]==numNo or (branche.getAttributs())[2]==numNo:
							listeBr.append(i)
						i+=1
					self.model.supprimePlusieursBranche(listeBr,numNo)
	def click1Mvt(self,evt):
		rayon=self.model.getRayon()
		liste=self.model.getListeNoeuds()
		if (noeudExiste(evt.x,evt.y,liste,2*rayon)):
			numNo=numNoeud(evt.x,evt.y,liste,rayon)
			if numNo>-1:
				if collision(numNo,evt.x,evt.y,liste,rayon)==False:
					self.model.repositionneUnNoeud(evt.x,evt.y,numNo)					
	def click3Mvt(self,evt):
		if self.model.getPositionClickDroit()==-1:
			self.model.setPositionClickDroit((evt.x,evt.y))
		else:
			xa=self.model.getPositionClickDroit()[0]
			ya=self.model.getPositionClickDroit()[1]
			for loop in self.model.getListeNoeuds():
				loop.setPosition(loop.getX()+evt.x-xa,loop.getY()+evt.y-ya)				
			self.model.setPositionClickDroit((evt.x,evt.y))
			self.model.actualise()
	def relache3(self,evt):
		self.model.setPositionClickDroit(-1)
