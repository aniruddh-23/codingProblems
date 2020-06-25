import math
import os
import random
import re
import sys

# Complete the maximumSum function below.
def binSearch(arr,val):
    #return element just greater than val
    #array is ascending order
    beg=0
    end=len(arr)    
    while end>beg:
        mid = (beg+end)//2
        print(mid)
        if arr[mid] == val:
            return arr[mid]
        elif arr[mid] < val:
            beg=mid+1
        elif arr[mid] > val:
            end=mid
    return -1
        
def binSearchGreater(arr,val):
    beg = 0
    end = len(arr)
    if len(arr)==1 or val>=arr[-2]:
        return arr[-1]
    while end>beg:
        mid = (beg+end)//2
        print(mid)
        if arr[mid] == val:
            break
        elif arr[mid] < val:
            beg=mid+1
        elif arr[mid] > val:
            end=mid
    mid = (beg+end)//2
    if arr[mid]>val:
        return arr[mid]
    return arr[mid+1]

def maximumSum(a, m):
    a = [i%m for i in a]
    sums = [a[0]]
    best = a[0]
    for i in range(1,len(a)):
        sums[i] = (sums[i]+a[i]%m)%m
        best = max((sums[i]-binSearchGreater(sums,sums[i])+m)%m,best)
    return best
    
        