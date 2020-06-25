# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:43:40 2020

@author: TheKa
"""

import sys
class Solution:
    def printDP(self,A,B,dp):
        b=['A']
        for i in B:
            b.append(i)
        print(b)
        for j in range(len(dp)):
            if j>0:
                print(A[j-1],dp[j])
            else:
                print('A',dp[j])
        
    def maxUncrossedLines(self, A, B):
        lines=[]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i]==B[j]:
                    lines.append((i,j))
        dp=[[0 for i in range(len(B)+1)] for j in range(len(A)+1)]

        for a in range(1,len(A)+1):
            for b in range(1,len(B)+1):
                val=max(dp[a-1][b],dp[a][b-1])
                if A[a-1]==B[b-1]:
                    val=max(val,dp[a-1][b-1]+1)
                for k in range(1,b):
                    if A[a-1]==B[k-1]:
                        val=max(val,dp[a-1][k-1]+1)
                for k in range(1,a):
                    if A[k-1]==B[b-1]:
                        val=max(val,dp[k-1][b-1]+1)
                dp[a][b]=val
        #self.printDP(A,B,dp)
        return dp,dp[len(A)][len(B)]
"""   
A=list(map(int,input().strip().split()))
B=list(map(int,input().strip().split()))

s=Solution()
print(s.maxUncrossedLines(A,B))
"""