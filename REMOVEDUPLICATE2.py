# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 00:50:28 2020

@author: MrMaak
"""

# Remove Duplicates from Sorted Array II
# Medium

# Given a sorted array nums, remove the duplicates in-place such that 
# duplicates appeared at most twice and return the new length.

# Do not allocate extra space for another array,
#  you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
    
# Given nums = [1,1,1,2,2,3],
# Your function should return length = 5,
#  with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It doesn't matter what you leave beyond the returned length.


# Example 2:
# Given nums = [0,0,1,1,1,1,2,3,3],
# Your function should return length = 7, 
# with the first seven elements of nums being modified 
# to 0, 0, 1, 1, 2, 3 and 3 respectively.
# It doesn't matter what values are set beyond the returned length.

def removedup2(nums):
    if len(nums)==0:
        return False
    i=0
    for j in nums:
        if nums[i]==j:
            i+=1
            nums[]




nums=[1,1,1,2,2,3]
print(removedup2(nums))
























