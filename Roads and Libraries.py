# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 11:11:18 2020

@author: TheKa
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
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

def roadsAndLibraries(n, c_lib, c_road, cities):
    #no of cities, cost lib, cost road, possibnle roads
    if c_road>c_lib:
        return c_lib*n
    S=subSets()
    for i in range(1,n+1):
        S.add(i)
    for i,j in cities:
        S.join(i,j)
    rt=S.joinedSets()
    print(rt)
    c=0
    for i in rt:
        c+=c_lib+c_road*(len(i)-1)
    return c
    #create min spanning forest and add number of libraries



q = int(input())

for q_itr in range(q):
    nmC_libC_road = input().split()

    n = int(nmC_libC_road[0])

    m = int(nmC_libC_road[1])

    c_lib = int(nmC_libC_road[2])

    c_road = int(nmC_libC_road[3])

    cities = []

    for _ in range(m):
        cities.append(list(map(int, input().rstrip().split())))

    result = roadsAndLibraries(n, c_lib, c_road, cities)
    print(result)

