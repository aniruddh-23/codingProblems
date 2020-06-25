# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 06:26:01 2020

@author: TheKa
"""
from itertools import combinations as C
import itertools

def posNegCount(arr):
    posCount = []
    negCount = []
    for i in arr:
        if i >= 0 :
            posCount.append(i)
        else :
            negCount.append(i)
    return posCount,negCount

def calVal(arr):
    pos,neg = posNegCount(arr)
    pos_ = []
    neg_ = []
    total = []
    for i in range(1,len(pos)+1):
        print("pos: ",list(C(pos,i)))
        pos_.append(list(C(pos,i)))
    for i in range(2,len(neg)+1,2):
        print("neg: ",list(C(neg,i)))
        neg_.append(list(C(neg,i)))
    for i in itertools.product(neg_,pos_):
        print(i)
        total.append(i)
    print(pos,neg)
    return total

data = [1,2,-2,-4]       
#data = list(map(int,input().strip().split(" ")))
print(calVal(data))