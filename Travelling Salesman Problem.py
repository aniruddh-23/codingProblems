# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:13:03 2020

@author: TheKa
"""
import sys
import copy
def cost(i,s,e):
    global adj_mat
    s.remove(i)
    #print(s)
    if len(s)==1:
        #print(i,s[0])
        return adj_mat[i][s[0]]+adj_mat[s[0]][e]
    else:
        c=sys.maxsize
        for j in s:
            c=min(c,cost(j,copy.deepcopy(s),e)+adj_mat[i][j])
        return c

T=int(input())

for _ in range(T):
    n=int(input())
    adj_mat=[]
    data=list(map(int,input().strip().split()))
    for i in range(n):
        adj_mat.append(data[i*n:(i+1)*n])

    s=[i for i in range(n)]
    c=sys.maxsize
    
    for i in range(n):
        #print(s)
        c=min(c,cost(i,copy.deepcopy(s),i))
    print(c)
    