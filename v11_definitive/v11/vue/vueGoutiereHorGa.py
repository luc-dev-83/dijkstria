#!/usr/bin/python
#-*- coding: UTF-8  -*-

from tkinter import *

class VueGoutiereHorGa(Frame):
	def __init__(self,parent,model,x,y):
		Frame.__init__(self,width=4*x/5-5,height=15,bg='blue')
		self.place(x=0,y=4*y/5)
		model.ajoutObservable(self)
	def adapte(self,model):
		self.place(x=0,y=model.hauteurCadreGauche)
		self.configure(width=model.largeurCadreGauche)
		
		
		
    
