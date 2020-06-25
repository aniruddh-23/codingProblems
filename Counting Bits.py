# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:24:20 2020

@author: TheKa
"""

import math
class Solution:
    def countBits(self, num) :
        bits=[None]*(num+1)
        bits[0]=0
        bits[1]=1
        v=1
        for i in range(2,num+1):
            if i==2**v:
                ln=i
                v+=1
            print(i,ln,i-ln,bits[i-ln])
            bits[i]=bits[i-ln]+1
        return bits

n=4
s=Solution()
print(s.countBits(n))