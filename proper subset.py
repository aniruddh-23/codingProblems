# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:10:25 2020

@author: TheKa
"""

def properSubsets(sub_set):
    proper_sub_set=[]
    sub_set.sort()
    proper_sub_set.append(sub_set[0])
    sub_set.remove(sub_set[0])
    for c1,c2 in sub_set:
        l_c1,l_c2 = proper_sub_set[-1]
        if c1<=l_c2:
            if c2>l_c2:
                proper_sub_set[-1] = (l_c1,c2)
        else:
            proper_sub_set.append((c1,c2))
    return proper_sub_set

a = [(1,2),(2,3),(4,5),(8,9),(10,20),(7,12)]
print(properSubsets(a))