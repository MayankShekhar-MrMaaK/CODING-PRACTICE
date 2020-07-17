# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:47:45 2020

@author: MrMaak
"""
#SUBSET SUM PROBLEM

#RECURSIVE APPROACH
def subrec(arr, s, n):
    #BASE CASE
    if s==0:
        return True
    if n==0 and s !=0:
        return False
    
    #CHOICE DIAGRAM
    if arr[n-1] > s:
        return subrec(arr, s, n-1)
    else:
        return ((subrec(arr, s-arr[n-1], n-1)) or (subrec(arr, s, n-1)))
    
#DP --> MEMORIZATION
def submem(arr, s, n):
    #BASE CASE
    if s==0:
        return True
    if n==0 and s !=0:
        return False
    
    if t[n][s] != -1:
        return t[n][s]
    
    #CHOICE DIAGRAM
    if arr[n-1] > s:
        t[n][s]= submem(arr, s, n-1)
        return t[n][s]
    else:
        t[n][s]= ((submem(arr, s-arr[n-1], n-1)) or (submem(arr, s, n-1)))
        return t[n][s]

#DP --> TOP-DOWN
def topdown(arr, s, n):
    for i in range(1,(s+1)):
        k[0][i]=False
    for i in range(n+1):
        k[i][0]=True
        
    for i in range(n+1):
        for j in range(s+1):
            if arr[i-1]> j:
                k[i][j]=k[i-1][j]
            else:
                k[i][j]= k[i-1][j-arr[i-1]] or k[i-1][j]
            
    return k[n][s]

arr=[1,2,3,5,14]
s=6
n=len(arr)
t=[[-1 for i in range(s+1)] for j in range(n+1)]
k=[[False for i in range(s+1)] for j in range(n+1)]

print("FOUND THE SUM RECURSIVE= {}? --> {}".format(s,subrec(arr,s, n)))
print("FOUND THE SUM MEMORIZATION= {}? --> {}".format(s,submem(arr,s, n)))
print("FOUND THE SUM TOPDOWN = {}? --> {}".format(s,topdown(arr,s,n)))