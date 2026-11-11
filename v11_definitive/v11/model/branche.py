class Branche:
	def __init__(self,obj):
		self.numA=obj[0]
		self.indA=obj[1]
		self.numB=obj[2]
		self.indB=obj[3]
		self.valeur=obj[4]
		self.couleur="black"
		if len(obj)==6:
			self.couleur=obj[5]
	def getAttributs(self):
		return (self.numA,self.indA,self.numB,self.indB,self.valeur,self.couleur)
	def setNumA(self,val):
		self.numA=val
	def setCouleur(self,val):
		self.couleur=val
	def getNumA(self):
		return self.numA
	def setNumB(self,val):
		self.numB=val
	def getNumB(self):
		return self.numB
	def getValeur(self):
		return self.valeur
