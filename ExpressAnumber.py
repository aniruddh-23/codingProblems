# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:24:17 2020

@author: TheKa
"""

t_list = {}
t_list[1] = 0 
def Enum(num):
    global t_list
    if num == 1:
        return t_list[1]
    else :
        total = 0
        for i in range(1,num):
            total += Enum(num-i) +1 
        t_list[num] = total
    return t_list[num]

def Enum2(num):
    t_list = {}
    t_list[1] = 0
    for i in range(2,num+1):
        total= 0
        for j in range(1,i):
            total+=t_list[i-j]+1
        t_list[i] = total
    return t_list[num]
