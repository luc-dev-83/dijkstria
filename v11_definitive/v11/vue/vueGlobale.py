#!/usr/bin/python
#-*- coding: UTF-8  -*-

from tkinter import *
from vue.cadreGauche import *
from vue.cadreGaucheBas import *
from vue.cadreDroitHaut import *
from vue.cadreDroitBas import *
from vue.vueGoutiere import *
from vue.vueGoutiereHorDr import *
from vue.vueGoutiereHorGa import *

class VueGlobale(Tk):
	def __init__(self,model):
		Tk.__init__(self)
		### Paramètre écran ###
		x=self.winfo_screenwidth()
		y=self.winfo_screenheight()
		self.geometry(str(x)+'x'+str(y)+'+0+0')
		self.overrideredirect(True) 
		### Cadres ###
		self.title("Graphe")
		self.cadreGauche=CadreGauche(self,model,x,y)
		self.cadreGaucheBas=CadreGaucheBas(self,model,x,y)
		self.vueGoutiere=VueGoutiere(self,model,x,y)
		self.vueGoutiereHorDr=VueGoutiereHorDr(self,model,x,y)
		self.vueGoutiereHorGa=VueGoutiereHorGa(self,model,x,y)
		self.cadreDroitHaut=CadreDroitHaut(self,model,x,y)
		self.cadreDroitBas=CadreDroitBas(self,model,x,y)
		model.ajoutObservable(self)
		model.setEcran(x,y,4*x/5)
		
	def adapte(self,model):
		self.cadreGauche.width=model.largeurCadreGauche-5
		self.cadreDroitHaut.width=model.largeurCadreGauche+5
		
		
		
    
