# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:55:34 2020

@author: TheKa
"""

# cook your dish here
T = int(input())
while T>0:
    T-=1
    n = int(input())
    line = list(map(int,input().split()))
    dist = 6
    flag = True
   # print(line)
    for i in line:
        if i == 1 :
            if dist >= 6:
                dist = 0
            else:
                #print("123")
                flag = False
               # print(flag)
                break
        dist+=1
    #print(flag)
    if flag:
        print("yes")
    else :
         print("no")
            