# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:32:23 2020

@author: TheKa
"""

"""
    workout = [0 for i in range(N+1)]
	workout[1] = 1
	for i in range(2,N+1):
		workout[i] = 1 + workout[i-1] + workout[i-2]
	print(workout[N]+1)
"""
#input_ = input().split("\n")
T = int(input())
#T = int(input_[0])
j = 0
while T>j :
    j+=1
    N=int(input())
    #N = int(input_[j])
    second_last = 1
    last = 2
    cur = last
    for i in range(2,N+1):
        #print(i)
        cur = last + second_last
        second_last = last
        last = cur
    print(cur)
