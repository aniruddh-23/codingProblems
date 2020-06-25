# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 07:37:14 2020

@author: TheKa
"""
import sys
beg=0
end=1000000
while end>beg:
    mid=(beg+end)//2 +1
    print(mid)
    sys.stdout.flush()
    res=input()
    if res=='<':
        end=mid-1
    else:
        beg=mid
mid=(beg+end)//2
print("!",mid)
sys.stdout.flush()