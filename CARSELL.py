# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:38:34 2020

@author: TheKa
"""

T = int(input())
while T>0:
    T-=1 
    n = int(input())
    cars = list(map(int,input().split()))
    time = 0
    profit = 0
    while len(cars)>0:
        max_ = max(cars)
        if max_ > time :
            profit+=max_-time
        cars.remove(max_)
        time+=1
    print(profit)
        