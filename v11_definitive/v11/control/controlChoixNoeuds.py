from tkinter import *
from tkinter.font import *

class ControlChoixNoeuds:
	def __init__(self, text1,text2,model,choix):
		self.choix=choix
		model.setLlisteNoeudsTraitement(("",""))
		model.setTraitement(9)
		self.model=model
		self.top = Toplevel(padx=(model.getLargeurEcran()-50)//2,pady=model.getHauteurEcran()//2)
		self.top.overrideredirect(True)
		self.top.title("Choix des noeuds")

		Label(self.top, text="Choix des noeuds").grid(column=0,row=0,columnspan=2)
		Label(self.top, text=text1).grid(column=0,row=1)
		self.e1 = Entry(self.top)
		self.e1.grid(column=1,row=1)
		if choix==2:													### choix du noeud de depart
			Label(self.top, text=text2).grid(column=0,row=2)
			self.e2 = Entry(self.top)
			self.e2.grid(column=1,row=2)
		
		noeuds=model.getListeNoeuds()
		listbox=Listbox(self.top)
		listbox.grid(column=2,row=1,rowspan=5)
		listbox.insert(END,"Noeuds existants")
		for noeud in noeuds:
			listbox.insert(END,noeud.getNom())
		
		Button(self.top, text="valider", command=self.ok).grid(column=1,row=3)
		Button(self.top, text="Annuler", command=self.pasOk).grid(column=0,row=3)	
	def ok(self):
		liste=self.model.getListeNoeuds()
		nom1=""
		nom2=""
		for loop in liste:
			if loop.getNom()==self.e1.get():
				 nom1=self.e1.get()
		if self.choix==2:
			for loop in liste:
				if loop.getNom()==self.e2.get() and loop.getNom()!=nom1:
					nom2=self.e2.get()
			if nom1!="" and nom2!="":
				self.model.setLlisteNoeudsTraitement((nom1,nom2))
				self.top.destroy()
		if self.choix==1:
			if nom1!="":
				self.model.setLlisteNoeudsTraitement((nom1,""))
				self.top.destroy()
	def pasOk(self):
		self.model.setTraitement(0)
		self.top.destroy()
		return -2      
