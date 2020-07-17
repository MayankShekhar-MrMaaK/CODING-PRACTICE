# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:24:44 2020

@author: MrMaak
"""

#SUBSET
# Given a set of distinct integers, nums, 
# return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]

# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

rtl=[]
def subset(alist, temp, start, end):
    rtl.append(temp)
    if start==end:
        return
    for i in range(start, end):
        subset(alist,temp+[alist[i]], i+1, end)
        
alist= [1,2,3]
subset(alist, [], 0, len(alist))
print(rtl)




