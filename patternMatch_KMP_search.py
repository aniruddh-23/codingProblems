# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 07:05:34 2020

@author: TheKa
"""

def makePatHash(pat):
    l = [0]*len(pat)
    i = 0
    for j in range(1,len(pat)):
        if(pat[i]==pat[j]):
            l[j] = i+1
            i+=1
        else:
            while i != 0:
                i = l[i-1]
                if(pat[i]==pat[j]):
                    l[j] = i+1
                    i+=1
                    break
    return l

def patSearch(input_,pat):
    l = makePatHash(pat)
    i = 0
    for j in range(len(input_)):
        if input_[j] == pat[i]:
            i+=1
        else :
            while i!=0:
                i = l[i-1]
                if input_[j] == pat[i]:
                    i+=1
                    break
                
        if i == len(pat):
            return (j-i+1,j)
    
    return 0
pat = "abcaby"
print(makePatHash(pat))
