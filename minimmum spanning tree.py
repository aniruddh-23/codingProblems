#User function Template for python3

# Function to construct and return cost of MST for a graph
# represented using adjacency matrix representation
'''
V: nodes in graph
E: number of edges in graph
graph: adjacency matrix, graph[i][j]=weight, if edge exits , else float("inf").
'''
def findDistance(in_set,not_in_set,graph,cost_value_set):
    for i in not_in_set:
        t_val = graph[i-1][in_set[-1]-1]
        if(cost_value_set[i] > t_val):
            #replace if new val less that old val
            cost_value_set[i] = t_val
    return cost_value_set

def findMimimum(not_in_set,cost_value_set):
    min_index = not_in_set[0]
    min_val = cost_value_set[min_index]
    for i in not_in_set:
        new_val = cost_value_set[i]
        if(new_val<min_val):
            min_val = new_val
            min_index = i
    return min_index
        
def spanningTree(V,E,graph):
    #code here
    in_set = []
    not_in_set = [i+1 for i in range(V)]
    cost_value_set = {}
    for i in not_in_set:
        cost_value_set[i] = float("inf")
    cost_value_set[not_in_set[0]] = 0
    cost = 0
    while len(in_set)<V:
        min_index = findMimimum(not_in_set,cost_value_set)
        not_in_set.remove(min_index)
        in_set.append(min_index)
        cost += cost_value_set[min_index]
        cost_value_set = findDistance(in_set,not_in_set,graph,cost_value_set)
      #  print(in_set,not_in_set)
    
    return cost
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        graph = [[float("inf") for i in range(V)] for i in range(V)]
        for i in range(0,len(info),3):
            u,v,w = info[i]-1,info[i+1]-1,info[i+2]
            graph[u][v] = w
            graph[v][u] = w
        print(spanningTree(V,E,graph))
# } Driver Code Ends