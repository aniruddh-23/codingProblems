# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:12:32 2020

@author: TheKa
"""
def printm(matrix):
    print( "   "+"  ".join([str(i) for i in range(1,len(matrix)+1)]))
    j = 1
    for i in matrix:
        print(j,end=" ")
        print(i)
        j+=1
def max_substring(s):
    matrix = [[0 for i in range(len(s))] for j in range(len(s))]
    max = 0
    for i in range(len(s)):
        matrix[i][i] = 1
        max = 1
    for i in range(1,len(s)):
        for beg,end in zip(range(0,len(s)-i),range(i,len(s))):
           # print(beg,end)
            if end-beg==1 and s[beg]==s[end]:
                matrix[beg][end]=2
                max = 2
            elif s[beg]==s[end] and matrix[beg+1][end-1]>0:
                matrix[beg][end]=matrix[beg+1][end-1]+2
                if matrix[beg][end]>max:
                    max = matrix[beg][end]
    printm(matrix)
    return max