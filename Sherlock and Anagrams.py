# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:16:00 2020

@author: TheKa
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    mat = {}
    len_s = len(s)
    anagrams = 0
    for i in range(len_s):
        for j in range(len_s):
            mat[(i,j)] = set()
            
        
    
    for first in range(len_s):
        for second in range(len_s):
            if s[first]==s[second] and first!=second:
                mat[(first,first)].add((second,second))
                beg = min(first,second)
                end = max(first,second)
                mat[(beg+1,end)].add((beg,end-1))
                mat[(beg,end-1)].add((beg+1,end))                
        anagrams += len(mat[(first,first)])
        
    for size in range(1,len_s):
        for beg in range(len_s-size):
            end = beg+size
            m1 = s[beg]
            m2 = s[end]
            if beg+1<=end:
                for beg_x,end_x in mat[(beg+1,end)]:
                    if beg_x>0 and beg_x-1!=beg and m1 == s[beg_x-1]:
                        mat[(beg,end)].add((beg_x-1,end_x))
                        if beg_x-2>beg and end+1>end_x:
                            mat[(beg,beg_x-2)].add((end+1,end_x))
                            mat[(end+1,end_x)].add((beg,beg_x-2))
                        
                    if end_x<len_s-1 and end_x+1!=end and m1 == s[end_x+1]:
                        mat[(beg,end)].add((beg_x,end_x+1))
                        if beg_x-2>beg and end+1>end_x:
                            mat[(beg,beg_x-2)].add((end+1,end_x))
                            mat[(end+1,end_x)].add((beg,beg_x-2))
            if beg<=end-1:
                for beg_x,end_x in mat[(beg,end-1)]:
                    if beg_x>0 and beg_x-1!=beg and  m2 == s[beg_x-1]:
                        mat[(beg,end)].add((beg_x-1,end_x))
                        if beg_x-2>beg and end+1>end_x:
                            mat[(beg,beg_x-2)].add((end+1,end_x))
                            mat[(end+1,end_x)].add((beg,beg_x-2))
                            
                    if end_x<len_s-1 and end_x+1!=end and m2 == s[end_x+1]:
                        mat[(beg,end)].add((beg_x,end_x+1)) 
                        if beg_x-2>beg and end+1>end_x:
                            mat[(beg,beg_x-2)].add((end+1,end_x))
                            mat[(end+1,end_x)].add((beg,beg_x-2))
            anagrams += len(mat[(beg,end)])
    for i in mat.keys():
        if len(mat[i])>0:
            print(i,mat[i])
    print(mat)
    return anagrams//2         
    

q = int(input())

for q_itr in range(q):
    s = input()

    result = sherlockAndAnagrams(s)

    print(str(result) + '\n')
