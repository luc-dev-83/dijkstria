#!/usr/bin/python
#-*- coding: UTF-8  -*-

from tkinter import *
from tkinter.font import *

class CadreDroitBas(Frame):
	def __init__(self,parent,model,x,y):
		Frame.__init__(self,width=x/5-5,height=y/5,bg='#c0c0c0')
		self.place(x=4*x/5+10,y=0)
		self.traitement=Canvas(self,width=x/5-20,height=y/5-25)
		self.traitement.place(x=5,y=5)
		model.ajoutObservable(self)
	def adapte(self,model):		
		self.configure(width=model.getLargeurEcran()-model.getLargeurCadreGauche()-9)
		self.configure(height=model.getHauteurEcran()-model.getHauteurCadreDroit()-15)
		self.place(x=model.getLargeurCadreGauche()+10,y=model.getHauteurCadreDroit()+15)
		self.traitement.configure(width=model.getLargeurEcran()-model.getLargeurCadreGauche()-24,
		height=model.getHauteurEcran()-model.getHauteurCadreDroit()-60)		
		self.saisiePointDepart=Entry(self.traitement,width=10)
		if model.getTraitement()==0:			
			self.traitement.delete(ALL)
			message="Mode conception"
			self.traitement.create_text(int(model.getLargeurCadreDroit()/2),model.getHauteurCadreDroitBas()//2,
			text=message,font=Font(family='Arial',size=14))
		if model.getTraitement() in (1,2) and model.getListeNoeudsTraitement()[0]=="":								#### getTraitement
			self.traitement.delete(ALL)
			message="Veuillez saisir le nom des noeuds"
			self.traitement.create_text(int(model.getLargeurCadreDroit()/2),model.getHauteurCadreDroitBas()//2,
			text=message,font=Font(family='Arial',size=14))
		elif model.getTraitement() in (3,4) and model.getListeNoeudsTraitement()[0]=="":								#### getTraitement
			self.traitement.delete(ALL)
			message="Veuillez saisir le nom du noeud de depart"
			self.traitement.create_text(int(model.getLargeurCadreDroit()/2),model.getHauteurCadreDroitBas()//2,
			text=message,font=Font(family='Arial',size=14))
		elif model.getTraitement() in (1,2,3):																		#### getTraitement
			self.traitement.delete(ALL)
			### Récupération des données
			xCadre=model.getLargeurCadreDroit()
			yCadre=model.getHauteurCadreDroitBas()
			listeNoeuds=model.getListeNoeudsTraitement()
			listeNoeudsModele=model.getListeNoeuds()
			nbrNoeud=len(listeNoeudsModele)
			listeNoms=[]
			for noeud in listeNoeudsModele:
				listeNoms.append(noeud.getNom())
			#####   titre
			if model.getTraitement() in (1,2):
				message="Dilkstra : plus court chemin de "+str(listeNoeuds[0])+" à "+str(listeNoeuds[1])
				self.traitement.create_text(int(xCadre/2),15,text=message,font=Font(size=12))
			elif model.getTraitement() in (3,4):
				message="Dilkstra : le noeud de départ est  "+str(listeNoeuds[0])
				self.traitement.create_text(int(xCadre/2),15,text=message,font=Font(size=12))
			##### Zone boutons - pieds de frame
			self.traitement.create_text(int(xCadre/2),int(yCadre-60),text="Suivant")

			#### Affichage du tableau
			nbrTours=model.getNbrTours()
			tableau=model.getTableauTravail()
			nLignes=len(tableau)
			if (model.getNbrTours()+1)//2==(model.getNbrTours()+1)/2:
				ymax=30+(min(model.getNbrTours()-1,2*nLignes-1)+4)//2*(yCadre-120)//(nbrNoeud+2)
			else:
				ymax=30+(min(model.getNbrTours()-1,2*nLignes-1)+4)//2*(yCadre-120)//(nbrNoeud+2)
			for i in range(nbrNoeud):
				self.traitement.create_line((i+1)*xCadre//(nbrNoeud+2),30,
				(i+1)*xCadre//(nbrNoeud+2),ymax,fill='black')	# vertical
				self.traitement.create_text(((i+1.5)*xCadre//(nbrNoeud+2))//1,
				(30+(0.5)*(yCadre-120)//(nbrNoeud+2))//1,text=str(listeNoms[i]))
			self.traitement.create_line((nbrNoeud+1)*xCadre//(nbrNoeud+2),30,
			(nbrNoeud+1)*xCadre//(nbrNoeud+2),ymax,fill='black') # vertical droite
			
			nbrTours=model.getNbrTours()
			tableau=model.getTableauTravail()
			
			self.traitement.create_line(xCadre//(nbrNoeud+2),30,
			(nbrNoeud+1)*xCadre//(nbrNoeud+2),30,fill='black')	# horizontal
			self.traitement.create_line(xCadre//(nbrNoeud+2),30+(yCadre-120)//(nbrNoeud+2),
			(nbrNoeud+1)*xCadre//(nbrNoeud+2),30+(yCadre-120)//(nbrNoeud+2),fill='black')	# horizontal
			
			
			for i in range((min(model.getNbrTours(),2*nLignes))):	
				if i//2==i/2:
					ligne=tableau[i//2]
					j=0
					for loop in ligne:
						if  model.getTraitement()==1:															### getTraitement
							self.traitement.create_text(((j+1.5)*xCadre//(nbrNoeud+2))//1,
							(23+(i/2+1.5)*(yCadre-120)//(nbrNoeud+2))//1,text=str(loop[0]))
							self.traitement.create_text(((j+1.5)*xCadre//(nbrNoeud+2))//1,
							(37+(i/2+1.5)*(yCadre-120)//(nbrNoeud+2))//1,text=str(loop[1]))
						elif model.getTraitement() in (2,3,4):													### getTraitement
							self.traitement.create_text(((j+1.5)*xCadre//(nbrNoeud+2))//1,
							(30+(i/2+1.5)*(yCadre-120)//(nbrNoeud+2))//1,text=str(loop[0]))
						j+=1
					self.traitement.create_line(xCadre//(nbrNoeud+2),30+(i+4)/2*(yCadre-120)//(nbrNoeud+2),
					(nbrNoeud+1)*xCadre//(nbrNoeud+2),30+(i+4)/2*(yCadre-120)//(nbrNoeud+2),fill='black')	# horizontal
			if model.getNbrTours()>2*nLignes and model.getTraitement() in (1,2):							### getTraitement
				self.traitement.create_text(int(xCadre/2),
				int(yCadre-80),text="Distance minimale : "+str(model.getReponse()[0])+
				"   Le trajet est  :  "+str(model.getReponse()[1]),font=Font(family='Arial',size=14))
		
		
		
		elif model.getTraitement()==4:					# Construction de l'arbre													### getTraitement
			if len(model.getTableauTravail())<1:
				self.traitement.delete(ALL)
				self.traitement.create_text(int(model.getLargeurCadreDroit()/2),model.getHauteurCadreDroit()//2,
				text="Tableau en cours de création",font=Font(family='Arial',size=14))
			else:
				self.traitement.delete(ALL)
				nbr=len(model.getReponse())
				largeurCadre=int(model.getLargeurCadreDroit())-50
				hauteurCadre=int(model.getHauteurCadreDroitBas())-50
				if model.getArbre().calculHauteur()==0:
					return 0 
				hauteurArbre=model.getArbre().calculHauteur()
				largeurArbre=model.getArbre().calculNbrFeuilles()
				arbre=model.getArbre()
				pasX=largeurCadre//(largeurArbre+4)
				pasY=hauteurCadre//(hauteurArbre+4)
				self.traitement.create_text(largeurCadre//2+25,pasY,
				text="Tracé de l'arbre de racine : "+model.getListeNoeudsTraitement()[0],
				font=Font(family='Arial',size=14))
				self.traitement.create_text(largeurCadre//2+25,pasY*(hauteurArbre+3),
				text="Noeuds non visités : "+model.getNoeudNonVisite(),
				font=Font(family='Arial',size=14))

				if arbre.getRacine().getNom()==None:
					pass
				else:
					self.__traceArbre(arbre,arbre.getRacine(),pasX,pasY)
		elif model.getTraitement()==5:
			pass ### trace en profondeur
		elif model.getTraitement()==6:
			''' trace en vertical '''
			if len(model.getTableauTravail())==0:
				return 0
			self.traitement.delete(ALL)
			largeurCadre=int(model.getLargeurCadreDroit())-50
			hauteurCadre=int(model.getHauteurCadreDroitBas())-50
			nbrLignes=len(model.getTableauTravail())+2
			pasY=hauteurCadre/nbrLignes
			self.traitement.create_text(largeurCadre//2+25,pasY,
			text="Tableau : parcous vertical. Départ : "+model.getListeNoeudsTraitement()[0],
			font=Font(family='Arial',size=14))
			
			maxi=len(model.getTableauTravail()[0])
			for i in range(len(model.getTableauTravail())):
				if maxi<len(model.getTableauTravail()[i]):
					maxi=len(model.getTableauTravail()[i])
			maxi+=2
			pasX=largeurCadre//maxi
			for i in range(len(model.getTableauTravail())):
				self.traitement.create_text(pasX+25,pasY*(i+2),
				text="L["+str(i)+"]",
				font=Font(family='Arial',size=14))
				for j in range(0,len(model.getTableauTravail()[i])):
					self.traitement.create_text((j+2)*pasX+25,pasY*(i+2),
					text=model.getTableauTravail()[i][j],
					font=Font(family='Arial',size=14))

					
			
			
			
			
	def __traceArbre(self,arbre,maillon,pasX,pasY):
		if maillon.getPositionVericale()==None:
			mgpv=0
		else:
			mgpv=maillon.getPositionVericale()
		xa=(mgpv+maillon.getNombreAncetreFeuille()//2+1)*pasX
		ya=(maillon.getProfondeur()+2)*pasY
		self.__traceMaillon(xa,ya,maillon.getNom(),str(maillon.getValeur()))
		if maillon.getPrecedent()!=None:
			if maillon.getPrecedent().getPositionVericale()==None:
				mgpv=0
			else:
				mgpv=maillon.getPrecedent().getPositionVericale()
			xd=(mgpv+maillon.getPrecedent().getNombreAncetreFeuille()//2+1)*pasX
			yd=(maillon.getPrecedent().getProfondeur()+2)*pasY
			self.traitement.create_line(xa,ya-12,xd,yd+22,fill='black',width=1)
			
		for i in range(len(maillon.getSuivants())):
			self.__traceArbre(arbre,maillon.getSuivants()[i],pasX,pasY)
	def __traceMaillon(self,xa,ya,nom,val):
		self.traitement.create_text(xa,ya-2,text=nom,font=Font(family='Arial',size=14))
		self.traitement.create_text(xa,ya+14,text=val,font=Font(family='Arial',size=14),fill='red')


