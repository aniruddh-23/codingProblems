# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:57:33 2020

@author: TheKa
"""
mod = 10^9+9
def booleanExpression(beg,end,val):
    global catalan_boolean
    if catalan_boolean[val][beg][end]==-1:
        value=0
        for i in range(beg,end):
            op=op_string[i]
            if val==1:
                if op=='o':
                     value+=booleanExpression(beg,i,1)*booleanExpression(i+1,end,1)
                     value+=booleanExpression(beg,i,0)*booleanExpression(i+1,end,1)
                     value+=booleanExpression(beg,i,1)*booleanExpression(i+1,end,0)
                elif op=='x':
                     value+=booleanExpression(beg,i,0)*booleanExpression(i+1,end,1)
                     value+=booleanExpression(beg,i,1)*booleanExpression(i+1,end,0)
                elif op=='a':
                     value+=booleanExpression(beg,i,1)*booleanExpression(i+1,end,1)
            else:
                if op=='a':     
                     value+=booleanExpression(beg,i,0)*booleanExpression(i+1,end,0)
                     value+=booleanExpression(beg,i,0)*booleanExpression(i+1,end,1)
                     value+=booleanExpression(beg,i,1)*booleanExpression(i+1,end,0)
                elif op=='o':
                     value+=booleanExpression(beg,i,0)*booleanExpression(i+1,end,0)
                elif op=='x':
                     value+=booleanExpression(beg,i,0)*booleanExpression(i+1,end,0)
                     value+=booleanExpression(beg,i,1)*booleanExpression(i+1,end,1)
        catalan_boolean[val][beg][end]=value%1000000009
    return catalan_boolean[val][beg][end]

bin_string,op_string=input().strip().split(" ")
bin_string = list(map(int,list(bin_string)))
op_string = list(op_string)

n=len(bin_string)

catalan_boolean = [[[-1 for i in range(n)] for j in range(n)] for k in range(2)]
#catlab brackets [1,2] 1,0 [0]
for i in range(n):
    catalan_boolean[bin_string[i]][i][i]=1
    catalan_boolean[1-bin_string[i]][i][i]=0
    
q=int(input())

for _ in range(q):
    beg,end,val = input().strip().split(" ")
    beg,end,val = int(beg)-1,int(end)-1,0 if val=="false" else 1
    print(booleanExpression(beg,end,val))