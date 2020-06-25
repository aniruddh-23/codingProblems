# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:43:36 2020

@author: TheKa
"""
import numpy as np

def dfs(node,adj_mat,non_visited,time):
    time_entry = time
    for i in non_visited:
        if adj_mat[i][node] == 1:
            non_visited.remove(i)
            non_visited,time = dfs(i,adj_mat,non_visited,time+1)
    time = time+1
    time_exit = time
    print(f"Node {node} Entry : {time_entry} Exit : {time_exit}")
    
    return non_visited,time
            

N = int(input().strip())
edges = list(map(int,input().strip().split(" ")))
adj_mat = np.zeros((N,N),dtype=int)
for i in range(0,len(edges),2):
    x = edges[i]
    y = edges[i+1]
    adj_mat[x][y]=1
    adj_mat[y][x]=1
non_visited =[i for i in range(1,N)]
dfs(0,adj_mat,non_visited,0)