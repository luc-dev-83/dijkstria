from tkinter import *
from PIL import Image, ImageTk


class Logo(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.title("Logo")
		
		
		self.image=Image.open("presentation/logo.png")
		self.photo = ImageTk.PhotoImage(self.image)
		
		self.canvas=Canvas(self, width=self.image.size[0], height=self.image.size[1],bg='grey')
		self.image.close()
		self.canvas.create_image(0,0,anchor= NW,image=self.photo)
		self.canvas.grid(column=0,row=1,columnspan=3)


		Button(self, text="Sortie", command=self.ok).grid(column=1,row=2)


	
	def ok(self):
		self.destroy()
		return 1
	
