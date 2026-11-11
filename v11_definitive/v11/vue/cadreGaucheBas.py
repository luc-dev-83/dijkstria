#!/usr/bin/python
#-*- coding: UTF-8  -*-

from tkinter import *

class CadreGaucheBas(Frame):
	def __init__(self,parent,model,x,y):
		Frame.__init__(self,width=4*x/5-5,height=y/10,bg='#c0c0c0')
		self.place(x=0,y=4*y/5)
		model.ajoutObservable(self)
		self.saisie=Entry(self,width=50)
		self.saisie.place(x=2*x/5-5,y=y/5-10)
		self.label=Label(self,text="Aucune instruction",width=50)
		self.label.place(x=2*x/5-5,y=y/10+10)
	def adapte(self,model):
		self.configure(width=model.largeurCadreGauche-5)
		self.configure(height=model.hauteurEcran-model.hauteurCadreGauche) 
		self.place(x=0,y=model.hauteurCadreGauche) 
		self.saisie.place(y=(model.hauteurEcran-model.hauteurCadreGauche)/2-15,
		x=(model.largeurCadreGauche-5)/3)
		self.label.place(y=(model.hauteurEcran-model.hauteurCadreGauche)/2+15,
		x=(model.largeurCadreGauche-5)/3)
		if model.getTraitement()==0:
			self.label.configure(text=model.getLabel())
		else:
			try:
				self.label.configure(text=(model.getTableauTravail()[model.getNbrTours()//2]))
			except:
				pass
