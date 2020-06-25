# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:03:09 2020

@author: TheKa
"""

#!/bin/python3

import math
import os
import random
import re
import sys



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
            print(1)
            print(k)
            k=self.key_parent[k]
        if self.key_parent[self.key[element]]!=-1: 
            self.key_parent[self.key[element]]=k
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

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    c = Connected()
    c.addMany([i for i in range(n)])
    for i,j in astronaut:
        c.join(i,j)
    seen = set()
    num_sets=c.connectedSetLen()
    r_sum=[sum(num_sets)]
    for i in num_sets:
        r_sum.append(r_sum[-1]-i)
    r_sum=r_sum[1:]
    pairs=0
    print(num_sets,r_sum)
    for i in range(len(num_sets)):
        pairs+=num_sets[i]*(r_sum[i])
    return pairs


