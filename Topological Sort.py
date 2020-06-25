# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:47:24 2020

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

def topo_sort(adj_mat):
    in_ = []
    not_in = list(i for i in range(len(adj_mat)))
    topo_stack = Stack()
    while len(not_in)>0:
        if(topo_stack.isEmpty()):
            r_index = random.randint(0,len(not_in)-1)
            topo_stack.push(not_in[r_index])
            not_in.remove(not_in[r_index])
        top = topo_stack.peek()
        flag = True
        for i in range(len(adj_mat)):
            if i in not_in and adj_mat[top][i] == 1:
                not_in.remove(i)
                topo_stack.push(i)
                flag = False
        if flag:
            print(topo_stack.pop())
                
  
N = int(input().strip())
edges = list(map(int,input().strip().split(" ")))
adj_mat = np.zeros((N,N),dtype=int)
for i in range(0,len(edges),2):
    x = edges[i]
    y = edges[i+1]
    adj_mat[x][y]=1
    
topo_sort(adj_mat)
