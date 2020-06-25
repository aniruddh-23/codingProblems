# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:46:24 2020

@author: TheKa
"""

import numpy as np
import random

class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        if(len(self.stack)==0):
            return True
        return False
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if self.isEmpty():
            return False
        value = self.stack[-1]
        self.stack = self.stack[:-1]
        return value
    def peek(self):
        if self.isEmpty():
            return False
        return self.stack[-1]

def max_histogram(arr):
    beg_stack= Stack()
    height_stack = Stack()
    arr.append(0)
    max_ = 0
    for i in range(0,len(arr)):
        if(beg_stack.isEmpty()):
            beg_stack.push(i)
            height_stack.push(arr[i])
        else :
            if arr[i] > height_stack.peek():
                height_stack.push(arr[i])#add new greater height
                beg_stack.push(i) #add begeining of new height
            elif  arr[i] < height_stack.peek():
                while arr[i] < height_stack.peek():
                    new_height = (i-beg_stack.pop())*height_stack.pop()
                    if new_height>max_:
                        max_ = new_height
                height_stack.push(arr[i])#add new greater height
                beg_stack.push(i) #add begeining of new height
    return max_

#arr = list(map(int,input().split()))
#arr = [1,2,5,1]
#print(max_histogram(arr))
                
                