# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 00:20:10 2020

@author: MrMaak
"""

s=5
arr=[1,2,3,5,10]
n=len(arr)

t=[[0 for j in range(s+1)] for i in range(n+1)]


for i in range(1, s+1):
    t[0][i]= 0
for i in range(n+1):
    t[i][0]= 1


for i in range(n+1):
    for j in range(s+1):
        
        if arr[i-1]> j:
            t[i][j]= t[i-1][j]
        else:
            t[i][j]= t[i-1][j-arr[i-1]] + t[i-1][j]
   
         
print(t[n][s])