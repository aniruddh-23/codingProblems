# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:15:09 2020

@author: TheKa
"""

def findIntersection(A,B):
    a_index,b_index=0,0
    intersection=[]
    while a_index<len(A) and b_index<len(B):
        a_s,a_e=A[a_index]
        b_s,b_e=B[b_index]
        
        if a_s>b_e:
            b_index+=1
            continue
        elif b_s>a_e:
            a_index+=1
            continue
        
        if a_s<b_s:
            #A starts firsts
            if a_e>=b_e:
                #A ends later
                intersection.append([b_s,b_e])
                b_index+=1
            elif a_e<b_e:
                #B ends later
                intersection.append([b_s,a_e])
                a_index+=1
        else:
            #B start first
            if a_e>=b_e:
                #A ends later
                intersection.append([a_s,b_e])
                b_index+=1
            elif a_e<b_e:
                #B ends later
                intersection.append([a_s,a_e])
                a_index+=1
    return intersection

        