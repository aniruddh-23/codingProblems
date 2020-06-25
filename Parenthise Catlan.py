# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:41:39 2020

@author: TheKa
"""

def Parenthsize(l,r):
    global paran
    if paran[l][r]==-1:
        value=0
        for i in range(l,r):
            #print(l,r)
            value+=Parenthsize(l,i)*Parenthsize(i+1,r)
        paran[l][r]=value
    return paran[l][r]

while True:
    n=int(input())
    paran=[[-1 for i in range(n)] for j in range(n)]
    for i in range(n):
        paran[i][i]=1
    print(Parenthsize(0,n-1))
        