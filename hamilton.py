# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:18:59 2020

@author: TheKa
"""

def canVisit(node,edge_data,visited):
    reachable = []
    for i in range(1,len(edge_data)):
        if i in visited:
            continue
        if edge_data[node-1][i-1]==1:
            reachable.append(i)
    return reachable

def do_hamilton(node,edge_data,visited):
    visited.append(node)
    if len(visited) == len(edge_data):
        return True
    reachable = canVisit(node,edge_data,visited)
    for i in reachable:
        if do_hamilton(i,edge_data,visited):
            return True
    return False

N = int(input().strip())
edges = list(map(int,input().strip().split()))
edge_data = np.zeros((N,N),dtype=int)
ans = "Not Possible"

for i in range(0,len(edges),2):
    x,y = edges[i]-1,edges[i+1]-1
    edge_data[x][y] = 1
    edge_data[y][x] = 1

for i in range(1,N+1):
    if do_hamilton(i,edge_data,[]):
        ans = "Possible"
        break
print(ans)