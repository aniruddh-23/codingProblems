# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:56:35 2020

@author: TheKa
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

def mod(x):
    return x%1000000007

#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#
f = math.factorial

def answerQuery(s,l, r):
    # Return the answer for this query modulo 1000000007.
    S = s[l-1:r]
    letters_list = {i:0 for i in set(S)}
    for i in S:
        letters_list[i]+=1
    ll_val = letters_list.values()
    double = [i//2 for i in ll_val if i>1]
    print(letters_list)
    print(double)
    single_len = 0
    for i in ll_val:
        single_len += i%2    
    total = f(sum(double))
    div = 1
    for i in double:
        if i == 1:
            continue
        div *= f(i)
    total = int(total/div)
    if single_len>0:
        total *= single_len
    return mod(total)



"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()


    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(s,l,r)

        fptr.write(str(result) + '\n')

    fptr.close()
    """
