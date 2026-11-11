#!/usr/bin/python
#-*- coding: UTF-8  -*-

from tkinter import *

class VueGoutiere(Frame):
	def __init__(self,parent,model,x,y):
		Frame.__init__(self,width=15,height=y,bg='blue')
		self.place(x=4*x/5-10,y=0)
		model.ajoutObservable(self)
	def adapte(self,model):
		self.place(x=model.largeurCadreGauche-5,y=0)
		
		
		
    
