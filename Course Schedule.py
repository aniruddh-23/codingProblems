# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:43:02 2020

@author: TheKa
"""

class Solution:
    def __init__(self):
        self.seen=set()
        self.waitq=set()
        self.pas=True
    
    def top(self,elm,parents):
        if not self.pas:
            return 
        for i in parents[elm]:
            if i in self.seen:
                continue
            if i in self.waitq:
                self.pas=False
                break
            self.waitq.add(i)
            self.top(i,parents)
            self.waitq.remove(i)
        self.seen.add(elm)
        
    def canFinish(self, numC, pre):
        parents={i:[] for i in range(numC)}        
        for i,j in pre:
            parents[j].append(i)
        for i in range(numC):
            if i not in self.seen:
                self.top(i,parents)
        return self.pas
            
numC=2
pre=[[1,0]]
s=Solution()
print(s.canFinish(numC,pre))