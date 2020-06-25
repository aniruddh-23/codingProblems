# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:14:00 2020

@author: TheKa
"""

from itertools import permutations as perm

def inverse(permutation):
     ans = []
     for i in range(1,len(permutation)+1):
             ans.append(permutation.index(i)+1)
     return ans
def sameInverse(n):
     Ps = list(perm([i for i in range(1,n+1)],n))
     #print(Ps)
     same=0
     for i in Ps:
             if list(i)==inverse(i):
                     same+=1
     return same

m = 10**9 + 7

def invCount(n):
    d={}
    d[1]=1
    d[2]=2
    for i in range(3,n+1):
        d[i] = (d[i-1]+d[i-2]*(i-1))%m
    return d[n]