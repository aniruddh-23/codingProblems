# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:55:13 2020

@author: TheKa
"""

class subSets:
    def __init__(self):
        self.parents={}
        self.id={}
        self.max=0
    def newNode(self):
        self.max+=1
        return self.max
    def add(self,elm):
        i=self.newNode()
        self.id[elm]=i
        self.parents[i]=i
    def parent(self,elm):
        e=self.id[elm]
        while e!=self.parents[e]:
            e=self.parents[e]
        return e
    def join(self,elm1,elm2):
        if elm1<elm2:
            self.parents[self.parent(elm2)]=self.parent(elm1)
        else:
            self.parents[self.parent(elm1)]=self.parent(elm2)
    def joinedSets(self):
        ps=[(i,self.parent(i)) for i in self.id]
        p={}
        for i,par in ps:
            if par not in p:
                p[par]=[]
            p[par].append(i)
        return list(p.values())