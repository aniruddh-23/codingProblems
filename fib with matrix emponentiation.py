# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:36:37 2020

@author: TheKa
"""


import numpy as np

def fib2(n):
    M = np.matrix([[1,1],[1,0]])
    A = np.matrix([[1,1],[1,0]])
    if n==0:
        return 0
    for i in range(2,n):
        A = np.matmul(A,M)
        #print(A)
    print(A)
    return A[0][0]

def fib(n):
    A = power(n-1)
    return A[0][0]
    

def mul(A,B):
    x = A[0][0]*B[0][0]+A[0][1]*B[1][0]
    y = A[0][0]*B[0][1]+A[0][1]*B[1][1]
    u = A[1][0]*B[0][0]+A[1][1]*B[1][0]
    v = A[1][0]*B[0][1]+A[1][1]*B[1][1]
    
    A[0][0] = x
    A[0][1] = y
    A[1][0] = u
    A[1][1] = v
    
    return A

def power(n):
    A = [[1,1],[1,0]]
    B = [[1,1],[1,0]]
    if n==1:
        return A
    powers = 2
    A = mul(A,B)
    while powers*2<n:
        powers=powers*2
      #  print(powers)
        A = mul(A,A)
       # print(A)
    while powers<n:
        powers+=1
        A = mul(A,B)
   # print(A)
    return A
        
    

"""
T = int(input())

while(T>0):
    T-=1
    n = int(input())
    print(fib(n)%1000000007)
"""

  

  
# Driver Code 
if __name__ == "__main__": 
    n = 100
    for n in [10,20,30,40,100,200]:
        print(fib(n)) 

