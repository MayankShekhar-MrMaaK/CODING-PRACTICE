# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 23:08:12 2020

@author: MrMaak
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#REMOVING DUPLICATE 1:
def removedup1():
    arr=[1,1,2]
    i=0
    for j in range(1, len(arr)):
        if arr[i]!= arr[j]:
            i+=1
            arr[i]=arr[j]
    print(i+1)



#REMOVING DUPLICATE 2:
# Given a sorted array nums, 
#remove the duplicates in-place such that duplicates 
#appeared at most twice and return the new length.

# Do not allocate extra space for another array, 
#you must do this by modifying the input array in-place
# with O(1) extra memory.

# Example 1:

# Given nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

# It doesn't matter what you leave beyond the returned length.
# Example 2:

# Given nums = [0,0,1,1,1,1,2,3,3],

# Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

#It doesn't matter what values are set beyond the returned length.
def removedup2():
    arr=[1,1,1,2,2,3]
    i=1
    for j in range(2, len(arr)):
        if arr[i-1]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    print(i+1)
    
    
#CALLING FUNCTION
print(removedup1())
print(removedup2())
    