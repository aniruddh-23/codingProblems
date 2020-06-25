# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 06:17:56 2020

@author: TheKa
"""

class stack:
    def __init__(self):
        self.stackarray = []
    def push(self,x):
        self.stackarray.append(x)
    def pop(self):
        if(len(self.stackarray)>0):
            val = self.stackarray[-1]
            self.stackarray = self.stackarray[:-1]
            return val
        else :
            return "Underflow"
    def isEmpty(self):
        if(len(self.stakarray)>0):
            return False
        return True
    def peek():
        if(len(self.stackarray)>0):
            return self.stackarray[-1]
        else :
            return "Underflow"
    