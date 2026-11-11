#!/usr/bin/python
#-*- coding: UTF-8  -*-

class MaillonDijkstra:
	def __init__(self,pNom,pValeur,pPrecedent):
		self.__nom=pNom
		self.__valeur=pValeur
		self.__suivant=[]
		self.__precedent=pPrecedent
		if pPrecedent==None:
			self.__profondeur=0
		else:
			self.__profondeur=pPrecedent.getProfondeur()+1
		
		self.__nombreAncetreFeuille=None
		self.__positionVericale=None
		
	### guetteur
	def getNom(self):
		return self.__nom
	def getValeur(self):
		return self.__valeur
	def getSuivants(self):
		return self.__suivant
	def getPrecedent(self):
		return self.__precedent
	def getProfondeur(self):
		return self.__profondeur
	def getNombreAncetreFeuille(self):
		return self.__nombreAncetreFeuille
	def getPositionVericale(self):
		return self.__positionVericale
	### setteur
	def setNom(self,pNom):
		self.__nom=pNom
	def setValeur(self,pValeur):
		self.__valeur=pValeur
	def setPrecedent(self,pPrecedent):
		self.__precedent=pPrecedent
	def setProfondeur(self,pProfondeur):
		self.__profondeur=pProfondeur
	def setNombreAncetreFeuille(self,val):
		self.__nombreAncetreFeuille=val
	def setPositionVericale(self,val):
		self.__positionVericale=val
	### Ajout
	def ajouteSuivant(self,maillon):
		self.__suivant.append(maillon)
