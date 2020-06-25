
class Solution:
    def possibleBipartition(self, N: int, dislikes) -> bool:
        g1,g2=set(),set()
        dis={i:[] for i in range(1,N+1)}
        color={i:-1 for i in range(1,N+1)}
        unseen=[i for i in range(1,N+1)]
        for i,j in dislikes:
            dis[i].append(j)
            dis[j].append(i)

        
        #print(dis)
        while len(unseen)>0:
            queue=[unseen[0]]
            cols=[0]
            unseen=unseen[1:]
            #col=0
            while len(queue)>0:
                print(queue,cols,color)
                col=cols[0]#color of current
                elm=queue[0]
                queue=queue[1:]
                cols=cols[1:]
                
                if color[elm]!=-1:
                    if color[elm]==col:
                        continue
                    else:
                        print(elm,col,color[elm],1)
                        return False
                color[elm]=col
                for j in dis[elm]:
                    if color[j]==-1:
                        queue.append(j)
                        cols.append((col^1))
                        if j in unseen:
                            unseen.remove(j)
                    elif color[j]==col:
                        print(2)
                        return False
        return True
            
            
                
N=10
dislikes=[[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]
s=Solution()
print(s.possibleBipartition(N,dislikes))