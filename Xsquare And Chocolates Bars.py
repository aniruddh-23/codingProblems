# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:37:49 2020

@author: TheKa
"""

input_data = input().split("\n")
#T = int(input())
T = int(input_data[0])
while T>0:
    T-=1
    #input_ = input()
    input_ = input_data[T+1]
    choclate_bar = [1 if i =="S" else 0 for i in input_]
    choclate_bar_end_list = [False for i in input_]
    choclate_bar_end_len = [0 for i in input_] 
    for end in range(2,len(input_)):
        if sum(choclate_bar[end-2:end+1]) in [1,2]:
            choclate_bar_end_list[end] = True
            if end-3 > 0:
                print(end,choclate_bar_end_list)
                choclate_bar_end_len[end] = choclate_bar_end_len[end-3]+3
            else :
                choclate_bar_end_len[end] = 3
    print( len(input_) - max(choclate_bar_end_len))
