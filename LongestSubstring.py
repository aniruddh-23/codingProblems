# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:14:33 2020

@author: TheKa
"""
def showMat(mat):
    for i in mat:
        print(i)
    print("\n\n")
        
def maxSubstring(s1,s2):
    subArray = []
    for i in range(len(s2)+1):
        subArray.append([0]*(len(s1)+1))
    for row in range(1,len(s2)+1):
        for col in range(1,len(s1)+1):
            if s1[col-1] == s2[row-1]:
                subArray[row][col] = subArray[row-1][col-1]+1
            else :
                subArray[row][col] = max(subArray[row][col-1],subArray[row-1][col])
        showMat(subArray)
    showMat(subArray)
    return subArray
            
def rTransverse(subArray,s1):
    row = len(subArray)-1
    col = len(subArray[0])-1
    val = subArray[row][col]
    maxSub = ''
    while val != 0:
        if subArray[row-1][col] == val:
            row = row -1
        elif subArray[row][col-1]==val:
            col = col-1
        else :
            maxSub = s1[col-1]+maxSub
            row = row -1
            col = col -1
            val = subArray[row][col]
            print(maxSub)
    return maxSub
s1 = "abcdaf"
s2 = "acbcf"
subArray = maxSubstring(s1,s2)
rTransverse(subArray,s1)