from tkinter import *
from PIL import Image, ImageTk


class Presentation(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.page=1
		self.title("Présentation")
		
		
		self.image=Image.open("presentation/0001.jpg")
		self.photo = ImageTk.PhotoImage(self.image)
		
		self.canvas=Canvas(self, width=self.image.size[0], height=self.image.size[1],bg='grey')
		self.image.close()
		self.canvas.create_image(0,0,anchor= NW,image=self.photo)
		self.canvas.grid(column=0,row=1,columnspan=3)

		Button(self, text="Suivant", command=self.suivant).grid(column=2,row=2)
		Button(self, text="Sortie", command=self.ok).grid(column=1,row=2)
		Button(self, text="Precedent", command=self.precedent).grid(column=0,row=2)

	
	def ok(self):
		self.destroy()
		return 1
	def suivant(self):
		self.page+=1
		if self.page==16:
			self.page=1
		self.afficher(self.page)
	def precedent(self):
		self.page-=1
		if self.page==0:
			self.page=15
		self.afficher(self.page)
	def afficher(self,i):
		self.canvas.delete(ALL)
		if i>9:
			self.image=Image.open("presentation/00"+str(i)+".jpg")
		else:
			self.image=Image.open("presentation/000"+str(i)+".jpg")
		self.photo = ImageTk.PhotoImage(self.image)
		self.canvas.create_image(0,0,anchor= NW,image=self.photo)
		self.image.close()

