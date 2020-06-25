# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:50:57 2020

@author: TheKa
"""

def maxCostPipeCut(costs,lengths,rod_len):
    cost_table = []
    for i in range(max(lengths)-min(lengths)+2):
        cost_table.append([0]*(rod_len+1))
   #show(cost_table)
    min_ = min(lenghts)
    for row in lengths:
        cut_len = row
        for col in range(rod_len+1):
            lenth_to_cut = col
            if(cut_len == min_):
                cost_table[row][col] = lenth_to_cut//cut_len*costs[cut_len]
            else :
                if cut_len>lenth_to_cut:
                    cost_table[row][col] = cost_table[row-1][col]
                else :
                   # show(cost_table)
                    print(row,row-1,col,col-cut_len,cut_len)
                    cost_table[row][col] = max(cost_table[row-1][col],cost_table[row][col-cut_len] + costs[cut_len] )
    return cost_table

def show(cost_table):
    print()
    for i in cost_table:
        print(i)
      
def r_crawl(cost_table,costs):
    val = cost_table[-1][-1]
    row = len(cost_table)-1
    col = len(cost_table[0])-1
    
    while val>0:
        if cost_table[row-1][col] == val:
            row = row-1
        else :
            print(row)
            col = col - row
            val = val -costs[row]
        
costs = [2,5,7,8]
lenghts = [1,2,3,4]
cost_ = {}
for i,j in zip(costs,lenghts):
    cost_[j] = i
costs = cost_
rod_len = 5

cost_table = maxCostPipeCut(costs,lenghts,rod_len)
show(cost_table)
r_crawl(cost_table,costs)
