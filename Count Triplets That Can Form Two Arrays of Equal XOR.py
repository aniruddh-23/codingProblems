# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:55:58 2020

@author: TheKa
"""

arr = list(map(int,input().strip().split(' ')))
xor_cumml = [0]
for i in range(0,len(arr)):
    xor_cumml.append(xor_cumml[-1]^arr[i])
trip = 0
#trips = []
for beg in range(1,len(arr)):
    for end in range(beg+1,len(arr)+1):
        for mid in range(beg+1,end+1):
            left=xor_cumml[mid-1]^xor_cumml[beg-1]
            right=xor_cumml[end]^xor_cumml[mid-1]
            if left==right:
                trip+=1
                #trips.append((beg-1,mid-1,end-1))
print(trip)
print(trips)