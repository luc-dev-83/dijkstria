#!/usr/bin/python
#-*- coding: UTF-8  -*-

from tkinter import *

class VueGoutiereHorDr(Frame):
	def __init__(self,parent,model,x,y):
		Frame.__init__(self,width=x/5-5,height=15,bg='blue')
		self.place(x=4*x/5+5,y=y/5)
		model.ajoutObservable(self)
	def adapte(self,model):
		self.place(x=model.largeurCadreGauche+10,y=model.hauteurCadreDroit)
		self.configure(width=model.largeurEcran-model.largeurCadreGauche-9)
		
		
		
    
