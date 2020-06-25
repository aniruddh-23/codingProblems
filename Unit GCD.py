# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:31:51 2020

@author: TheKa
"""

# cook your dish here
def gen_primes(N):
    primes = [i for i in range(2,N+1)]
    #print(primes)
    index = 0
    while index<len(primes):
        prime = primes[index]
        #print(prime)
        index+=1
        i = index
        while i<len(primes):
            if primes[i]%prime == 0:
                primes.remove(primes[i])
            else:
                i+=1
    return primes 
    
def factors(n,primes):
    fact = set([n])
    for i in primes:
        if n%i ==0:
            fact.add(i)
        if i>n:
            break
    return fact


def cofactor(a,b,factor_list):
    fa = factor_list[a]
    fb = factor_list[b]
   # print(len(fa-fb))
   # print(len(fb-fa) )
    #rint(len(fa-fb)+len(fb-fa) == 0)
    return len(fa.intersection(fb)) == 0
    
T = int(input())

for _ in range(T):
    N = int(input())
    pages = [i+1 for i in range(N)]
    primes = gen_primes(N)
    #print(primes)
    factor_list = {i:factors(i,primes) for i in pages}
    #print(factor_list)
    turn = []
    while(len(pages)>0):
        this_turn=[]
        pages_t = pages[:]
        index = 0
        while index<len(pages_t):
            entry = pages_t[index]
            index += 1
            this_turn.append(entry)
            pages.remove(entry)
            #print(pages,pages_t)
            pages_t = [i for i in pages_t if cofactor(entry,i,factor_list) or entry==i] #i%entry==0 means that entry devides i
            #print(pages_t)
        turn.append(this_turn)
    
    for i in turn:
        print(len(i),end=" ")
        for j in i:
            print(j,end=" ")
        print()
        
            