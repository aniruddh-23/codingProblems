# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:17:41 2020

@author: TheKa
"""

def no_of_one(n):
    ones = 0
    while n>0:
        print(n,n&(n-1))
        n = n&(n-1)
        ones+=1
    return ones