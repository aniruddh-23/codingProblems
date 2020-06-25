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

mat = {}

def updateMat(sub_string,anagram):
    global mat
    mat[sub_string].add(anagram)
    mat[anagram].add(sub_string)
    #print(sub_string,anagram)
    sub_beg,sub_end = sub_string
    ana_beg,ana_end = anagram
    
    #add pairs in bw
    
    if ana_end>sub_end+1 and ana_beg-1>sub_beg:
        mat[(sub_end+1,ana_end)].add((sub_beg,ana_beg-1))
        mat[(sub_beg,ana_beg-1)].add((sub_end+1,ana_end))
    elif sub_end>ana_end+1 and sub_beg-1>ana_beg:
        mat[(ana_end+1,sub_end)].add((ana_beg,sub_beg-1))
        mat[(ana_beg,sub_beg-1)].add((ana_end+1,sub_end))

        
    #add symmetric pairs

def sherlockAndAnagrams(s):
    global mat
    mat = {}
    
    #initatialise mat
    len_s = len(s)
    for i in range(len_s):
        for j in range(len_s):
            mat[(i,j)]=set()
    for first in range(len_s):
        for second in range(len_s):
            if first!= second and s[first]==s[second]:
                updateMat((first,first),(second,second))
   
            
    for sub_string_len in range(1,len_s):
        for sub_string_beg in range(0,len_s-sub_string_len):
            sub_string_end = sub_string_beg+sub_string_len
            l_char = s[sub_string_beg]
            r_char = s[sub_string_end]
            #2 past anagrams to consider
            
            l_anagram_beg,l_anagram_end = sub_string_beg,sub_string_end-1 # match r_char
            r_anagram_beg,r_anagram_end = sub_string_beg+1,sub_string_end # match l_char
            
            

            for sub_anagram_beg,sub_anagram_end in mat[(l_anagram_beg,l_anagram_end)]:
                #match with anagrams if left substring
                if sub_anagram_beg-1>=0 and sub_anagram_beg-1!=sub_string_beg and s[sub_anagram_beg-1]==r_char:
                    updateMat((sub_string_beg,sub_string_end),(sub_anagram_beg-1,sub_anagram_end))
                if sub_anagram_end+1<len_s and sub_anagram_end+1!=sub_string_end and s[sub_anagram_end+1]==r_char:
                    updateMat((sub_string_beg,sub_string_end),(sub_anagram_beg,sub_anagram_end+1))
        

            for sub_anagram_beg,sub_anagram_end in mat[(r_anagram_beg,r_anagram_end)]:
                #match with anagrams of right substring
                if sub_anagram_beg-1>=0 and sub_anagram_beg-1!=sub_string_beg and s[sub_anagram_beg-1]==l_char:
                    updateMat((sub_string_beg,sub_string_end),(sub_anagram_beg-1,sub_anagram_end))
                if sub_anagram_end+1<len_s and sub_anagram_end+1!=sub_string_end and s[sub_anagram_end+1]==l_char:
                    updateMat((sub_string_beg,sub_string_end),(sub_anagram_beg,sub_anagram_end+1))
    
    count=0
    for i in mat:
        if len(mat[i])>0:
            count += len(mat[i])
            print(i,mat[i])
    return count//2      
    

q = int(input())

for q_itr in range(q):
    s = input()

    result = sherlockAndAnagrams(s)

    print(str(result) + '\n')