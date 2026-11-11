#!/usr/bin/python
#-*- coding: UTF-8  -*-
from control.fonctionsGraphe import *
from math import *

class ControlCadreGaucheBas:
	def __init__(self,vue,model):
		self.model=model
		self.vue=vue
		self.vue.saisie.bind("<Return>",self.entree)
	def entree(self,evt):
		message=self.vue.saisie.get()
		self.model.setLabel(eval(message))
	
