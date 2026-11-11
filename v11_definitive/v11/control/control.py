#!/usr/bin/python
#-*- coding: UTF-8  -*-

from control.controlGoutiere import *
from control.controlGoutiereHorDr import *
from control.controlGoutiereHorGa import *
from control.controleurMenu import *
from control.controlCadreGaucheHaut import *
from control.controlCadreDroitBas import *
from control.controlCadreGaucheBas import *

class Control:
	def __init__(self,vue,model):
		self.model=model
		self.vue=vue
		self.controlGoutiere=ControlGoutiere(vue.vueGoutiere,model)
		self.controlGoutiereDroit=ControlGoutiereHorDr(vue.vueGoutiereHorDr,model)
		self.controlGoutiereGauche=ControlGoutiereHorGa(vue.vueGoutiereHorGa,model)
		self.controleurMenu=ControleurMenu(vue,model)
		self.controlCadreGaucheHaut=ControlCadreGaucheHaut(vue.cadreGauche,model)
		self.controlCadreDroitBas=ControlCadreDroitBas(vue.cadreDroitBas.traitement,model)
		self.controlCadreGaucheBas=ControlCadreGaucheBas(vue.cadreGaucheBas,model)
