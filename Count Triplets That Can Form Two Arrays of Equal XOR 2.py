# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:20:04 2020

@author: TheKa
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:55:58 2020

@author: TheKa
"""

arr = list(map(int,input().strip().split(' ')))
xor_cumml = [0]
for i in range(0,len(arr)):
    xor_cumml.append(xor_cumml[-1]^arr[i])
mids_arr = [{} for i in range(len(arr)+1)]
trip = 0
#trips = []
for mid in range(2,len(arr)+1):
    #mid should be atlewst the 2nd element and here elements start at 1
    for beg in range(1,mid):
        #till 1 less than mid
        value = xor_cumml[mid-1]^xor_cumml[beg-1]
        if value not in mids_arr[mid].keys():
            mids_arr[mid][value]=0
        mids_arr[mid][value]+=1
        

for mid in range(2,len(arr)+1):
    for end in range(mid,len(arr)+1):
        value=xor_cumml[end]^xor_cumml[mid-1]
        if value in mids_arr[mid].keys():
            trip+=mids_arr[mid][value]

print(trip)
print(trips)