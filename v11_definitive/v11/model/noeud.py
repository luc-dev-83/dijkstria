class Noeud:
	def __init__(self,obj,nbrCo):
		### Obj : Position x ; position y ; nom ; 
		self.x=obj[0]
		self.y=obj[1]
		self.nom=obj[2]
		self.style=0
		### 0 : Noeud classique ; 1 : Marqueur des liaisons possibles
		self.nbrConnections=[0]*nbrCo
		self.nbrConnect=nbrCo
		self.couleur='black'
		if len(obj)>3:
			self.style=obj[3]
			self.couleur=obj[4]
			self.nbrConnect=obj[5]
			self.nbrConnections=obj[6]
		

		
### Mutateur
	def setPosition(self,px,py):
		self.x=px
		self.y=py
	def setNumCarre(self,val,num):				### Indice , valeur
		self.nbrConnections[val]=num
	def setStyle(self,val):
		self.style=val
	def setCouleur(self,val):
		self.couleur=val
		
### Guetteur
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getNom(self):
		return self.nom
	def getPosition(self):
		return (self.x,self.y)
	def getNumCarre(self,num):
		return self.nbrConnections[num]
	def getNbrConnection(self):
		return self.nbrConnect
	def getStyle(self):
		return self.style
	def getCouleur(self):
		return self.couleur
