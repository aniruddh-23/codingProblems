# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:05:36 2020

@author: TheKa
"""

class Connected:
    def __init__(self):
        self.key={}
        self.key_parent={}
        self.issued_keys=0
        
    def newKey(self):
        self.issued_keys+=1
        self.key_parent[self.issued_keys]=-1
        return self.issued_keys
    
    def parent(self,element):
        k=self.key[element]
        while self.key_parent[k]!=-1:
            k=self.key_parent[k]
        return k
    def add(self,i):
        self.key[i]=self.newKey()
    def addMany(self,arr):
        for i in arr:
            self.add(i)
            
    def join(self,i,j):
        """
        k=set(self.key.keys())
        if i in k and j not in k:
            self.key[j]=self.key[i]
            return 0
        if i not in k and j in k:
            self.key[i]=self.key[j]
            return 0
        if i not in k and j not in k:
            self.key[i]=self.key[j]=self.newKey()
            return 0
        """
        self.key_parent[self.parent(max(i,j))]=self.parent(min(i,j))
        return 0
    
    def connectedSet(self):
        for i in self.key.keys():
            self.key[i]=self.parent(i)
        k = set(self.key.values())
        conn_set = {i:[] for i in k}
        for i in self.key.keys():
            conn_set[self.key[i]].append(i)
        return conn_set
    
    def connectedSetLen(self):
        for i in self.key.keys():
            self.key[i]=self.parent(i)
        k = set(self.key.values())
        conn_set = {i:0 for i in k}
        for i in self.key.keys():
            conn_set[self.key[i]]+=1
        #print(conn_set)
        return [i for i in conn_set.values()]
    

        
        
            