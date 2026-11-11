#!/usr/bin/python
#-*- coding: UTF-8  -*-

class Observable:
    def __init__(self):
        self.listeObservable={}
    def ajoutObservable(self,obj):
        self.listeObservable[obj]=1
    def actualise(self):
        for loop in self.listeObservable:
            loop.adapte(self)
    
