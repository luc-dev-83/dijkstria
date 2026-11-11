#!/usr/bin/python
#-*- coding: UTF-8  -*-
from model.modele import *
from vue.vueGlobale import *
from control.control import *

from tkinter.font import *


model=Modele()
vue=VueGlobale(model)
control=Control(vue,model)
vue.mainloop()
