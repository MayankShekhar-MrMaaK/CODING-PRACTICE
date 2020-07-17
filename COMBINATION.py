# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:23:51 2020

@author: MrMaak
"""

'''Given two integers n and k, 
return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]'''


rst=[]
def possible(curr,start):
    if len(curr)==k:
        rst.append(curr)
        return
    for i in range(start,n+1):
        possible(curr+[i],i+1)

n,k=4,2
possible([],1)
print(rst)








