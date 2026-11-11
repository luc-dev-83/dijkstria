#!/usr/bin/python
#-*- coding: UTF-8  -*-

class ControlGoutiereHorDr:
	def __init__(self,vue,model):
		self.model=model
		self.vue=vue
		self.vue.bind("<B1-Motion>",self.click1Mvt)
	def click1Mvt(self,evt):
		self.model.setEcranDroit(evt.y-5)
