# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:12:59 2020

@author: TheKa
"""

class Solution:
    def exhaustHeight(self,edges_dict,node,n):
        height = 0
        
        #rem.remove(node)
        queue = [(i,1) for i in edges_dict[node]]
        rem = [i for i in range(n) if i not in edges_dict[node]]
        rem.remove(node)
        while len(queue)>0:
            elm = queue[0]
            added=True
            for i in edges_dict[elm[0]]:
                print(node,queue)
                if i in rem:
                    added=False
                    rem.remove(i)
                    queue.append((i,elm[1]+1))
            if added and elm[1]>height:
                height=elm[1]
            queue = queue[1:]
        return height
    def findMinHeightTrees(self, n, edges):
        if n==1:
            return [0]
        edges_dict = {i:[] for i in range(n)}
        for i,j in edges:
            edges_dict[i].append(j)
            edges_dict[j].append(i)
        min_trees_root=[]
        heights = []
        for i in range(n):
            heights.append(self.exhaustHeight(edges_dict,i,n))
        height = min(heights)
        print(heights)
        for i in range(n):
            if heights[i]==height:
                min_trees_root.append(i)
                
        return min_trees_root
    
S = Solution()