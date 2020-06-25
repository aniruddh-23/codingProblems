# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:18:40 2020

@author: TheKa
"""
def show(mat):
    for i in mat:
        print(i)
    print("\n\n")
        
def reverse_transverse(value_array,s1,s2):
    row = len(value_array)-1
    col = len(value_array[0])-1
    val = value_array[row][col]

    
    while val!= 0:
      #  print(row,col,val,"Vals",value_array[row-1][col-1],value_array[row][col-1],value_array[row-1][col])
        if value_array[row-1][col-1] == val:
            print((value_array[row-1][col-1] == val),val,value_array[row-1][col-1],":",0)
            row = row-1
            col = col-1
        elif value_array[row-1][col-1] < val:
            print(value_array[row-1][col-1] < val,val,value_array[row-1][col-1],":",1)
            print(f"{s2[row]}->{s1[col]}")
            val = value_array[row-1][col-1] 
            row = row-1
            col = col-1
        elif value_array[row][col-1] < val:
            print(value_array[row][col-1] < val,val,value_array[row][col-1],":",2)
          #  print(f"add({s1[col-1]})")
            print(f"remove({s2[row-1]})")
            val = value_array[row][col-1] 
            col = col-1
        elif value_array[row-1][col] < val:
            print(value_array[row-1][col] < val,val,value_array[row-1][col],":",3)
            #print(f"remove({s2[row-1]})")
            print(f"add({s1[col-1]})")
            val = value_array[row-1][col]
            row  =row -1
    show(value_array)
            
def minEdit(s1,s2):
    ##initialisation
    value_array = []
    for i in range(len(s2)+1):
        value_array.append([0]*(len(s1)+1))
    for row in range(len(s2)+1):
        value_array[row][0] = row
    for col in range(len(s1)+1):
        value_array[0][col] = col
    
    for row in range(1,len(s2)+1):
        for col in range(1,len(s1)+1):
            if(s2[row-1]==s1[col-1]):
                value_array[row][col] = value_array[row-1][col-1]
            else :
                value_array[row][col] = min(value_array[row-1][col-1],value_array[row][col-1],value_array[row-1][col])+1
        show(value_array)
    reverse_transverse(value_array,s1,s2)
        
minEdit("xabc","abc")
        