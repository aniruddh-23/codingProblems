'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import sys
def mst(edges,V):
    unseen=set(i for i in range(2,V+1))
    seen=[1]
    cost=0
    dist={i:sys.maxsize for i in range(2,V+1)}
    print(dist)
    while len(unseen)>0:
        #dist=[]
        for i in unseen:
            m=sys.maxsize
            for j in seen:
                if edges[i][j]!=None:
                    print(edges[i][j])
                    m=min(m,edges[i][j])
            dist[i]=min(m,dist[i]) 
        seen=[]
        #min in dist
        val=min(dist.values())
        for i in dist:
            if dist[i]==val:
                val=i
                break
        
        #add to sseen and remove from unseen
        print(unseen,dist)
        seen.append(val)
        unseen.remove(val)
        # add cost to cost
        cost+=dist[val]
        dist.pop(val)
    return cost

#V,E=map(int,input().strip().split())
V,E=4,5
edges=[[None for i in range(V+1)] for j in range(V+1)]
#for _ in range(E):
 #   x,y,v=map(int,input().strip().split())
  #  edges[x][y]=v 
   # edges[y][x]=v
tbs=[[1,2,7],[1,4,6],[4,2,9],[4,3,8],[2,3,6]]
for x,y,v in tbs:
   edges[x][y]=v 
   edges[y][x]=v
print(mst(edges,V))
