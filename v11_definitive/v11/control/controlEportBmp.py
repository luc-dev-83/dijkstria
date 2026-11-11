from tkinter import *
from tkinter.font import *
from os import listdir 
import tkinter.messagebox
from PIL import Image, ImageGrab
import os.path


class ControlExportBmp(Toplevel):
	def __init__(self, prompt,model):
		Toplevel.__init__(self)
		self.model=model
		listeFichiers=listdir("imageBmp")
		self.geometry("400x260+500+50")
		self.title("Choix du nom de l'image")
		self.frame=Frame(self,width=390,height=250)
		
		Label(self.frame,text="Choix du nom de l'image ",font=Font(size=16)).grid(column=0,row=0,columnspan=2)
		Label(self.frame, text=prompt).grid(column=0,row=2)
		self.nomFichier = Entry(self.frame)
		self.nomFichier.grid(column=1,row=2)
		
		listbox=Listbox(self.frame)
		listbox.grid(column=2,row=2)
		listbox.insert(END,"Images existantes")
		for fichier in listeFichiers:
			listbox.insert(END,fichier)
		
		
		Button(self.frame, text="valider", command=self.ok).grid(column=1,row=3)
		Button(self.frame, text="Annuler", command=self.pasOk).grid(column=0,row=3)
		self.frame.pack()
	
	def ok(self):
		a,b,c,d = 0 , 20 , self.model.getLargeurCadreGauche() - 5 , self.model.getHauteurCadreGauche()+20
		obFichier = self.__capture(a,b,c,d,"imageBmp/"+self.nomFichier.get()+".bmp")
		self.destroy()
		return 1
	def pasOk(self):
		self.destroy()
		return -2  	
	def __capture(self,a,b,c,d,nom):
		im=ImageGrab.grab(bbox=(a,b,c,d))
		im.save(nom)    
