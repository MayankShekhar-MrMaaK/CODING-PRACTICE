# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:15:49 2020

@author: MrMaak
"""

''' Given a set of characters and a positive integer k, 
possibleint all possible strings of length k that can be formed 
from the given set.
Input: 
set[] = {'a', 'b'}, k = 3

Output:
aaa
aab
aba
abb
baa
bab
bba
bbb


Input: 
set[] = {'a', 'b', 'c', 'd'}, k = 1
Output:
a
b
c
d
'''

rst=[]
def possible(curr):
  if len(curr)==k:
    rst.append(curr)
    return
  for i in aset:
    possible(curr+i)
        
aset={'a','b','c'}
k=3
possible("")
print(rst)