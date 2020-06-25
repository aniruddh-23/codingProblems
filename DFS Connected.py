
N,M=map(int,input().split(' '))
edges={i:[] for i in range(1,N+1)}
for _ in range(N):
	x,y=map(int,input().split(' '))
	edges[i].append(j)
	edges[j].append(i)
h=int(input())
stack=[]
seen=set()
stack.append(h)
seen.add(h)

while len(stack())>0:
    top=stack[-1]
    seen.add(top)
    ls=len(stack)
    for i in edges[top]:
        if i in seen:
            continue
        top.append(i)
        break
    if len(stack)>ls:
        stack=stack[:-1]
print(N-len(seen))  
		

