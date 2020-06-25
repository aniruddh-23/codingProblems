# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 20:33:04 2020

@author: TheKa
"""

class Queue:
    def __init___(self):
        self.queue = []
    def add(self,x):
        self.queue.append(x)
    def add_list(self,list_):
        for x in list_:
            self.add(x)
    def isEmpty(self):
        return not len(self.queue)>0
    def get(self):
        if self.isEmpty():
            return False
        val = self.queue[0]
        self.queue = self.queue[1:]
        return val
    def peek(self):
        if self.isEmpty():
            return False
        return self.queue[0]
    
def canReach(pos,reach_list):
    x = pos[0]
    y = pos[1]
    reachable = []
    increment_list = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    for i in increment_list:
        t_x = x+i[0]
        t_y = y+i[1]
        if(t_x>8 or t_y>8 or t_x<1 or t_y<1 or reach_list[(t_x,t_y)]):
            continue
        reach_list[(t_x,t_y)] = True
        reachable.append((x,y))
    return reachable

if __name__ == "main":
    beg = tuple(map(int,input().split()))
    end = tuple(map(int,input().split()))
    reach_list = {}
    for x in range(1,9):
        for y in range(1,9):
            reach_list[(x,y)] = False
    reach_list[beg] = True
    distance = 0
    while not reach_list[end]:
        first = reach_list.get()
        reach_list.add_list(canReach(first,reach_list))
        
        
        
        
    

        