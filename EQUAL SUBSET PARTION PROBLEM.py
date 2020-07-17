# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:47:00 2020

@author: MrMaak
"""
# EQUAL SUBSET PARTION PROBLEM
#Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Note:

# Each of the array element will not exceed 100.
# The array size will not exceed 200.
 

# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

# Example 2:

# Input: [1, 2, 3, 5]

# Output: false

# Explanation: The array cannot be partitioned into equal sum subsets.


def recc(nums, s, n):
    if s==0:
        return True
    if n==0 and sum!=0:
        return False
    
    if t[n][s]!=- 1:
        return t[n][s]
    
    if nums[n-1]>s:
        t[n][s]= recc(nums, s, n-1)
        return t[n][s]
    else:
        t[n][s]= (recc(nums, s-nums[n-1], n-1) or recc(nums, s, n-1))
        return t[n][s]

def canPartition(nums) -> bool:
    s=sum(nums)
    if s%2!=0:
        return False
    else:
        s//=2
        n=len(nums)
        k=[[False for i in range(s+1)] for j in range(n+1)]
        for i in range(n+1):
            k[i][0]=True
        for i in range(1,s+1):
            k[0][i]= False
        for i in range(n+1):
            for j in range(s+1):
                if nums[i-1]> j:
                    k[i][j] = k[i-1][j]
                else:
                    k[i][j]= k[i-1][j-nums[i-1]] or k[i-1][j]        
        return k[n][s]
        
nums=[1,5,11,5]
s=sum(nums)
n=len(nums)
t=[[-1 for i in range(s+1)] for j in range(n+1)]
a1=recc(nums, s//2, n)
a=canPartition( nums)
print(a1)
