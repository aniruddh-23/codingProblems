# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:03:31 2020

@author: TheKa
"""

import queue
import numpy as np 

#dfs_stack = queue.LifoQueue()
dfs_stack = []

N = int(input().strip())
edges = list(map(int,input().strip().split(" ")))
start_node = int(input().strip())

#dfs_stack.put(start_node)
dfs_stack.append(start_node)
adj_mat = np.zeros((N,N),dtype=int)
flag = True

for i in range(0,len(edges),2):
    x = edges[i]
    y = edges[i+1]
    adj_mat[x][y]=1
    adj_mat[y][x]=1
color = [None]*N
color[start_node] = 1
#print(not stack.empty())

#while not stack.empty():
while len(dfs_stack)>0 and flag:
    #top = stack.get()
    top = dfs_stack[-1]
    dfs_stack.remove(top)
    print(color)
    for i in range(N):
        if adj_mat[top][i] == 1:
            if color[i] == None:
                color[i] = (1+color[top])%2
                #stack.put(i)
                dfs_stack.append(i)
            elif color[i] == color[top]:
                print("Not Bipartite")
                flag = False
                break
if(flag):
    print("Bipartite")
    
                
    