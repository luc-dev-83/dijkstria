from tkinter import *
from tkinter.font import *
from os import listdir

class ControlSauveModel:
	def __init__(self, prompt,model):
		self.model=model
		listeFichiers=listdir("sauvegardeTxt")
		self.top = Toplevel(padx=(model.getLargeurEcran()-50)//2,pady=model.getHauteurEcran()//2)
		self.top.overrideredirect(True)
		self.top.title("Choix du nom de fichier")
		
		Label(self.top,text="Choix du nom de fichier ",font=Font(size=16)).grid(column=0,row=0,columnspan=2)
		Label(self.top, text=prompt).grid(column=0,row=2)
		self.nomFichier = Entry(self.top)
		self.nomFichier.grid(column=1,row=2)
		
		listbox=Listbox(self.top)
		listbox.grid(column=2,row=2)
		listbox.insert(END,"Fichiers existants")
		for fichier in listeFichiers:
			listbox.insert(END,fichier)
		
		
		Button(self.top, text="valider", command=self.ok).grid(column=1,row=3)
		Button(self.top, text="Annuler", command=self.pasOk).grid(column=0,row=3)
	
	def ok(self):
		obFichier = open("sauvegardeTxt/"+self.nomFichier.get()+".txt",'w')
		obFichier.write(str(int(self.model.getLargeurEcran()))+"\n")
		obFichier.write(str(int(self.model.getHauteurEcran()))+"\n")
		obFichier.write(str(int(self.model.getLargeurCadreGauche()))+"\n")
		obFichier.write(str(int(self.model.getHauteurCadreDroit()))+"\n")
		obFichier.write(str(int(self.model.getHauteurCadreGauche()))+"\n")

		obFichier.write(str(int(self.model.getRayon()))+"\n")
		obFichier.write(str(int(self.model.getPas()))+"\n")
		obFichier.write(str(int(self.model.getNbrCo()))+"\n")
		
		listeDeuxNoeuds=self.model.getListeDeuxModeles()
		obFichier.write(str(listeDeuxNoeuds[0])+"\n")
		obFichier.write(str(listeDeuxNoeuds[1])+"\n")
		
		obFichier.write(str(len(self.model.getListeNoeuds()))+"\n")
		for i in range(len(self.model.getListeNoeuds())):
			noeud=(self.model.getListeNoeuds())[i]
			obFichier.write(str(noeud.getX())+"\n")
			obFichier.write(str(noeud.getY())+"\n")
			obFichier.write(str(noeud.getNom())+"\n")
			obFichier.write(str(noeud.getStyle())+"\n")
			obFichier.write(str(noeud.getCouleur())+"\n")
			obFichier.write(str(noeud.getNbrConnection())+"\n")
			for j in range(noeud.getNbrConnection()):
				obFichier.write(str(noeud.getNumCarre(j))+"\n")
		listeBranche=self.model.getListeBranche()
		obFichier.write(str(len(listeBranche))+"\n")
		for branche in listeBranche:
			attributs=branche.getAttributs()
			for loop in attributs:
				obFichier.write(str(loop)+"\n")
		obFichier.close()
		self.top.destroy()
		return 1
	def pasOk(self):
		self.top.destroy()
		return -2      
