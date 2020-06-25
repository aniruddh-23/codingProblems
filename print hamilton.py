# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:54:47 2020

@author: TheKa
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:18:59 2020

@author: TheKa
"""

def canVisit(node,edge_data,visited):
    reachable = []
    for i in range(1,len(edge_data)+1):
        if i in visited:
           # print("A")
            continue
        #print("B")
        if edge_data[node-1][i-1]==1:
            reachable.append(i)
    return reachable

def do_hamilton(node,edge_data,visited,path):
    t_visited = visited[:]
    t_visited.append(node)
    path = path+f"->{node}"
   # print(visited,t_visited)
    if len(t_visited) == len(edge_data):
        return path,True
    reachable = canVisit(node,edge_data,t_visited)
    #print(node,visited,path,reachable)
    for i in reachable:
        t_path, bool_value = do_hamilton(i,edge_data,t_visited,path)
        if bool_value:
            return t_path,True
    return "",False

N = int(input().strip())
edges = list(map(int,input().strip().split()))
edge_data = np.zeros((N,N),dtype=int)
ans = "Not Possible"

for i in range(0,len(edges),2):
    x,y = edges[i]-1,edges[i+1]-1
    edge_data[x][y] = 1
    edge_data[y][x] = 1

for i in range(1,N+1):
    t_path, bool_value = do_hamilton(i,edge_data,[],"")
    print(i,bool_value)
    if bool_value:
        print(f"path: {t_path}")
        ans = ""
    
print(ans)