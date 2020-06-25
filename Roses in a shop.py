# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:21:36 2020

@author: TheKa
"""

n = int(input())
roses = list(map(int,input().strip().split(" ")))
sequences = []
seqence = 1
for i in range(1,n):
    if roses[i]>roses[i-1]:
        seqence+=1
    else:
        sequences.append(seqence)
        seqence=1
max_smell = max(sequences)
for i in range(2,len(sequences)):
    if sequences[i-1]==1 and sequences[i]+sequences[i-2]>max_smell:
        max_smell = sequences[i]+sequences[i-2]
print(max_smell)