# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:39:59 2020

@author: TheKa
"""

def findMax(arr,start,end) -> int:
    if start==end:
        return (arr[start],start)
    mid = (start+end)//2
    return max(findMax(arr,start,mid),findMax(arr,mid+1,end))

a=[1231,2342,24,123,5454,-2,34234,2191,32,342,65]
print(findMax(a,0,len(a)-1))
    