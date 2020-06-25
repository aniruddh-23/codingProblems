# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:07:37 2020

@author: TheKa
"""

#code

def  changeAlignment(a,c):
    if a == 's' :
        if c=='r':
            a = 'w'
        else :
            a = 'e'
            
    elif a=='e':
        if c=='r':
            a = 's'
        else :
            a = 'n'
            
    elif a== 'n':
        if c== 'r':
            a = 'e'
        else :
            a = 'w'
    
    elif a=='w':
        if c=='r':
            a = 'n'
        else :
            a = 's'
            
    return a
            
def isCircular(moves):
    align = 's'
    up = 0
    left = 0
    
    for i in moves:
        if i in ['r','l']:
            align = changeAlignment(align,i)
        else :
            if align == 's':
                up -= 1
            elif align == 'n':
                up +=1
            elif align == 'e':
                left += 1
            else :
                left -= 1
    if up == 0 and left ==0 :
        return "Circular"
    else :
        return "Not Circular"
    
T = int(input())
while T>0:
    T-=1
    moves = list(input().strip().lower())
    print(isCircular(moves))