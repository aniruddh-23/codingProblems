# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 08:32:06 2020

@author: TheKa
"""
import numpy as np

class DoubleStack:
    def __init__(self,size=10):
        self.arr = np.empty(size,dtype=int)
        self.size = size
        self.topA = size
        self.topB = -1
    def isFull(self):
        if(self.topB+(size-self.topA) == size-1):
            return True
        return False
    
    def pushA(self,value):
        if(self.isFull()):
            print("Overflow!")
        else :
            self.topA-=1
            arr[self.topA] = value
    def popA(self):
        if(self.topA == self.size):
            print("A underflow")
        else:
            self.topA += 1
            return self.arr[self.topA-1]
    
    def pushB(self,value):
        if(self.isFull()):
            print("Overflow!")
        else :
            self.topB+=1
            arr[self.topB] = value
    def popB(self):
        if(self.topB == -1):
            print("A underflow")
        else:
            self.topB -= 1
            return self.arr[self.topB+1]
    
        