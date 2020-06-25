# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:12:28 2020

@author: TheKa
"""

def show(mat):
    for i in mat:
        print(i)
    print("\n\n")
        
def isDevidable(data):
    total = sum(data)
    value2reach = total/2
    value_array = []
    for i in range(len(data)+1):
        value_array.append([False]*value2reach)
        