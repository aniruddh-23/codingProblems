# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:59:29 2020

@author: TheKa
"""

# cook your dish here

mod=1000000007

def posPatterts(mask,t):
    global dp
    #print(mask,t,(1<<n)-1)
    if mask==(1<<n)-1:
        return 1
    if t==101:
        return 0
    if dp[mask][t]!=None:
       return dp[mask][t]

    val = 0
    
    for i in r_map[t]:
        #print(mask,mask&(1<<i),mask|(1<<i),mask&(1<<i) == (1<<i))
        if mask&(1<<i) == (1<<i):
            continue
        val+=posPatterts((mask|(1<<i)),t+1)
    val+=posPatterts(mask,t+1)#dont give t
    dp[mask][t]=val%mod
    #return dp[mask][t]
    return val
T=int(input())

for _ in range(T):
    n=int(input())
    tshirts=[]
    for i in range(n):
        tshirts.append(list(map(int,input().strip().split())))
    r_map={i:[] for i in range(1,101)}
    for i in range(n):
        for j in tshirts[i]:
            r_map[j].append(i)
    #dp=[[None]*101]*(2**n)
    
    print(posPatterts(0,1))
    
                