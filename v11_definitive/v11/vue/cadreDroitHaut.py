#!/usr/bin/python
#-*- coding: UTF-8  -*-

from tkinter import *
from tkinter.font import *

class CadreDroitHaut(Frame):
	def __init__(self,parent,model,x,y):
		Frame.__init__(self,width=x/5-5,height=4*y/5-15,bg='#c0c0c0')
		self.place(x=4*x/5+10,y=y/5+15)		
		self.solution=Canvas(self,width=x/5-20,height=4*y/5)
		self.solution.place(x=5,y=5)
		self.model=model
		model.ajoutObservable(self)
	def adapte(self,model):
		self.configure(width=model.largeurEcran-model.largeurCadreGauche-9)
		self.configure(height=model.hauteurCadreDroit)
		self.place(x=model.largeurCadreGauche+10,y=0)		
		self.solution.configure(width=model.getLargeurEcran()-model.getLargeurCadreGauche()-24,
		height=model.getHauteurCadreDroit()-15)
		
		if model.getTraitement()==0:
			self.solution.delete(ALL)
			message="Mode conception"
			self.solution.create_text(int(model.getLargeurCadreDroit()/2),model.getHauteurCadreDroit()//2,
			text=message,font=Font(family='Arial',size=14))
		if model.getTraitement() in (1,2) and model.getListeNoeudsTraitement()[0]=="":								#### getTraitement
			self.solution.delete(ALL)
			message="Veuillez saisir le nom des noeuds"
			self.solution.create_text(int(model.getLargeurCadreDroit()/2),model.getHauteurCadreDroitBas()//2,
			text=message,font=Font(family='Arial',size=14))
		elif model.getTraitement() in (3,4) and model.getListeNoeudsTraitement()[0]=="":							#### getTraitement
			self.solution.delete(ALL)
			message="Veuillez saisir le nom du noeud de depart"
			self.solution.create_text(int(model.getLargeurCadreDroit()/2),model.getHauteurCadreDroitBas()//2,
			text=message,font=Font(family='Arial',size=14))
		elif model.getTraitement() in (1,2) and len(model.getTableauTravail())<1:
			self.solution.delete(ALL)
			self.solution.create_text(int(model.getLargeurCadreDroit()/2),model.getHauteurCadreDroit()//2,
			text="Tableau en cours de création",font=Font(family='Arial',size=14))
		elif model.getTraitement() in (1,2):																		### getTraitement
			self.solution.delete(ALL)
			self.solution.create_text(int(model.getLargeurCadreDroit()/2),model.getHauteurCadreDroit()//2,
			text="Distance minimale : "+str(self.model.getReponse()[0])+
			"   Le trajet est  :  "+str(self.model.getReponse()[1]),font=Font(family='Arial',size=14))
		elif model.getTraitement()in (3,4):																		### getTraitement
			if len(model.getTableauTravail())<1:
				self.solution.delete(ALL)
				self.solution.create_text(int(model.getLargeurCadreDroit()/2),model.getHauteurCadreDroit()//2,
				text="Tableau en cours de création",font=Font(family='Arial',size=14))
			else:
				self.solution.delete(ALL)
				i=0
				nbr=len(self.model.getReponse())

				
					
				for loop in self.model.getReponse():
					try:
						if i==0:
							self.solution.create_text(int(model.getLargeurCadreDroit()/2),10+i*15,
							text="Trajets possibles à partir de : "+model.getListeNoeudsTraitement()[0]+"   : ",
							font=Font(family='Arial',size=14))
						elif i==1:
							self.solution.create_text(50,30+i*18,
							text="Destination",font=Font(family='Arial',size=12))
							self.solution.create_text(150,30+i*18,
							text="Distance",font=Font(family='Arial',size=12))
							self.solution.create_text(350,30+i*18,
							text="Trajet",font=Font(family='Arial',size=12))
						elif i>0:							
							self.solution.create_text(50,30+i*18,
							text=str(loop[1][len(loop[1])-1]),font=Font(family='Arial',size=12))
							self.solution.create_text(150,30+i*18,
							text=str(loop[0]),font=Font(family='Arial',size=12))
							self.solution.create_text(350,30+i*18,
							text=str(loop[1]),font=Font(family='Arial',size=12))
							
							
							self.solution.create_line(10,21+i*18,500,21+i*18,fill='black')
							self.solution.create_line(10,39,500,39,fill='black')
							self.solution.create_line(10,21+nbr*18,500,21+nbr*18,fill='black')
							self.solution.create_line(10,39,10,21+nbr*18,fill='black')
							self.solution.create_line(100,39,100,21+nbr*18,fill='black')
							self.solution.create_line(200,39,200,21+nbr*18,fill='black')
							self.solution.create_line(500,39,500,21+nbr*18,fill='black')
							self.solution.create_text(100,40+nbr*18,
							text="Noeuds non visités : ",
							font=Font(family='Arial',size=14))
							self.solution.create_text(350,40+nbr*18,
							text=self.model.getNoeudNonVisite(),
							font=Font(family='Arial',size=14))
					except:
						
						self.solution.create_text(int(model.getLargeurCadreDroit()/2),model.getHauteurCadreDroit()//2,
						text="Tableau en cours de création",font=Font(family='Arial',size=14))
					i+=1
