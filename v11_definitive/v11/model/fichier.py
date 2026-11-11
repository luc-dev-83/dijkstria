from tkinter.filedialog import *
from control.controlSauveModel import *
from control.controlEportJpg import *
from control.controlEportBmp import *






def choixFichier():
	try:
		fichier=askopenfilename(title="choix du fichier",
		filetypes=(("Text files", "*.txt"),("All files", "*.*")))
		return fichier
	except:
		return -2
def chargeModel(model):
	monFichier=choixFichier()
	try:
		obFichier=open(monFichier,'r')
	except:
		return 0
	texte=(obFichier.read()).split("\n")
	model.setLargeurEcran(int(texte[0]))
	model.setHauteurEcran(int(texte[1]))
	model.setLargeurCadreGauche(int(texte[2]))
	model.setHauteurCadreDroit(int(texte[3]))
	model.setHauteurCadreGauche(int(texte[4]))	
	model.setRayonSauv(int(texte[5]))
	model.setPasSauv(int(texte[6]))
	model.setNbrCoSauv(int(texte[7]))
	model.setListeDeuxNoeuds(int(texte[8]),int(texte[9]))

	nbrNoeud=int(texte[10])
	compteur=11
	if nbrNoeud>0:
		for k in range(nbrNoeud):
			px=int(texte[compteur])
			compteur+=1
			py=int(texte[compteur])
			compteur+=1
			pNom=texte[compteur]
			compteur+=1
			pStyle=int(texte[compteur])
			compteur+=1
			pCouleur=texte[compteur]
			compteur+=1
			pNbrConnection=int(texte[compteur])
			liste=[]
			compteur+=1
			for u in range(pNbrConnection):
				liste.append(int(texte[compteur]))
				compteur+=1
			model.ajouterNoeud((px,py,pNom,pStyle,pCouleur,pNbrConnection,liste))
	nbrBranches=int(texte[compteur])
	if nbrBranches>0:
		compteur+=1
		for k in range(nbrBranches):
			model.ajouteBranche((int(texte[compteur]),
			int(texte[compteur+1]),
			int(texte[compteur+2]),
			int(texte[compteur+3]),
			int(texte[compteur+4]),
			texte[compteur+5]))
			compteur+=6
	model.actualise()
	obFichier.close()



def sauverModel(model):
	choixFichier=ControlSauveModel("Nom du fichier :",model)
	
def ExporterJpg(model): 
	choixFichier=ControlExportJpg("Nom du fichier :",model)
def ExporterBmp(model):  
	choixFichier=ControlExportBmp("Nom du fichier :",model)





if __name__=="__main__":
	from os import chdir
	chdir("..\sauvegardeTxt")

	obFichier = open('Monfichier.txt','w')
	obFichier.write("Bonjour,\n fichier !\n")
	obFichier.write("Quel beau temps, aujourd'hui !")
	obFichier.close()

	obFichier = open('Monfichier.txt','r')
	text=(obFichier.read()).split("\n")
	print(text)
	for ligne in text:
		print(ligne)
	obFichier.close()
