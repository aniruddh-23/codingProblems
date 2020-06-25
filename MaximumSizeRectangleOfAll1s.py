# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:59:40 2020

@author: TheKa
"""

from maxHistogram import max_histogram
import numpy as np

def findMaxOnes(beg,arr):
    max_=0
    t_arr= [0]*(len(arr))
    flag = True
    for col in range(beg,len(arr[0])):
        for row in range(0,len(arr)):
            if flag:
                t_arr[row] = arr[row][col]
            elif t_arr[row]==0:
                continue
            else :
                t_arr[row] = t_arr[row]*arr[row][col] + arr[row][col] #becomes zero if arr[row][col] is zero
        flag = False
        max_t = max_histogram(t_arr)
        if(max_t>max_):
            max_=max_t
    return max_

def maxOneRectangle2(arr):
    max_=0
    t_arr= [0]*(len(arr))
    for col in range(0,len(arr[0])):
        for row in range(0,len(arr)):
            if arr[row][col]==0:
                t_arr[row] = 0
            else :
                t_arr[row] += 1
            #becomes zero if arr[row][col] is zero
        max_t = max_histogram(t_arr)
        if(max_t>max_):
            max_=max_t
    return max_
def maxOneRectangle(arr):
    max_=0
    for i in range(0,len(arr[0])):
        max_t = findMaxOnes(i,arr)
        if max_t>max_:
            max_ = max_t
    return max_


#arr = [[1,0,0,1,1,1],[1,0,1,1,0,1],[0,1,1,1,1,1],[0,0,1,1,1,1]]
arr = [[0,0,1,1],[1,1,1,1],[1,1,1,0],[0,1,1,1]]
print(maxOneRectangle(arr))
print(maxOneRectangle2(arr))