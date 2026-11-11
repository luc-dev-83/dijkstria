#!/usr/bin/python
#-*- coding: UTF-8  -*-

from tkinter import *
from math import *
from tkinter.font import *

class CadreGauche(Frame):
	def __init__(self,parent,model,x,y):
		Frame.__init__(self,width=4*x/5-5,height=4*y/5,bg='#c0c0c0')
		self.graphe=Canvas(self,width=4*x/5-20,height=4*y/5-30)
		self.graphe.place(x=5,y=5)
		self.place(x=0,y=0)
		self.label=Label(self,text="Saisie :",font=Font(size=9))
		self.label.place(x=2*x/5-40,y=4*y/5-35)
		self.saisie=Entry(self,width=20)
		self.saisie.place(x=2*x/5-20,y=4*y/5-25)
		self.model=model
		model.ajoutObservable(self)
	def getSaisie(self):
		return self.saisie.get()
	def adapte(self,model):
		### Adaptation du modele
		self.configure(width=model.largeurCadreGauche-5)
		self.configure(height=model.hauteurCadreGauche)
		self.graphe.delete(ALL)
		self.graphe.configure(width=model.largeurCadreGauche-20)
		self.graphe.configure(height=model.hauteurCadreGauche-15) 
		self.saisie.place(x=(model.largeurCadreGauche)/2,y=model.hauteurCadreGauche-25)
		self.label.place(x=(model.largeurCadreGauche)/2-44,y=model.hauteurCadreGauche-27)
		### Adaptation du graphe
		r=model.getRayon()
		rp=r/5
		compteur=0
		for loop in model.getListeNoeuds():
			px=loop.getX()
			py=loop.getY()
			nc=loop.getNbrConnection()
			self.graphe.create_oval(px-r,py-r,px+r,py+r,outline=loop.getCouleur(),width=1)
			if compteur==(model.getListeDeuxModeles())[0]:
				self.graphe.create_text(px,py,text=loop.getNom(),font=Font(size=int(10*r//15)),fill='green')
			elif compteur==(model.getListeDeuxModeles())[1]:
				self.graphe.create_text(px,py,text=loop.getNom(),font=Font(size=int(10*r//15)),fill='red')
			else:
				self.graphe.create_text(px,py,text=loop.getNom(),font=Font(size=int(10*r//15)),fill='black')
			compteur+=1
			if loop.getStyle()==1:
				for i in range(nc):
					x=px+r*cos(2*pi*i/nc)
					y=py+r*sin(2*pi*i/nc)
					if loop.getNumCarre(i)==0:
						self.graphe.create_rectangle(x-rp,y-rp,x+rp,y+rp,width=1)
					if loop.getNumCarre(i)==1:
						self.graphe.create_oval(x-rp,y-rp,x+rp,y+rp,outline="red",width=1)
					if loop.getNumCarre(i)==2:
						pass
		cte=8
		for loop in self.model.getListeBranche():
			parametre=loop.getAttributs()
			liste=self.model.getListeNoeuds()
			noeud1=liste[parametre[0]]
			noeud2=liste[parametre[2]]
			x1=noeud1.getX()+r*cos(2*pi*parametre[1]/noeud1.getNbrConnection())
			y1=noeud1.getY()+r*sin(2*pi*parametre[1]/noeud1.getNbrConnection())
			x2=noeud2.getX()+r*cos(2*pi*parametre[3]/noeud2.getNbrConnection())
			y2=noeud2.getY()+r*sin(2*pi*parametre[3]/noeud2.getNbrConnection())
			d=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
			self.graphe.create_oval(x1-3,y1-3,x1+3,y1+3,fill=parametre[5],width=1)
			self.graphe.create_oval(x2-3,y2-3,x2+3,y2+3,fill=parametre[5],width=1)
			self.graphe.create_line(x1,y1,x2,y2,fill=parametre[5],width=1)
			self.graphe.create_line(x1-cte*(x1-x2)//d-cte*(y1-y2)//d,y1-cte*(y1-y2)//d+cte*(x1-x2)//d,x1,y1,fill=parametre[5],width=1)
			self.graphe.create_line(x1-cte*(x1-x2)//d+cte*(y1-y2)//d,y1-cte*(y1-y2)//d-cte*(x1-x2)//d,x1,y1,fill=parametre[5],width=1)
			
			
			self.graphe.create_text((x1+x2)/2,(y1+y2)/2,text=parametre[4],font=Font(size=int(10*r//15)))
