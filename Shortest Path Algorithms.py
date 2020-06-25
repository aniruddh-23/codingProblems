# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 07:02:32 2020

@author: TheKa
"""

import sys
def bellmanFord(edges,V):
    dist=[sys.maxsize for i in range(V+1)]
    dist[1]=0
    for _ in range(V+1):
     for x,y,v in edges:
            dist[y] = min(dist[y],dist[x]+v)
    return dist[2:]



edges=[(1,2,5),(1,3,2),(3,4,1),(1,4,6),(3,5,5)]
V=5

print(bellmanFord(edges,V))