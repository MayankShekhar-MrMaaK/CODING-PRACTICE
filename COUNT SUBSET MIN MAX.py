# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 00:50:42 2020

@author: MrMaak
"""
''' Input:

Given an array A of
-positive
-sorted
-no duplicate
-integer

A positive integer k


Output:

Count of all such subsets of A,
Such that for any such subset S,
Min(S) + Max(S) = k
subset should contain atleast two elements

1. Backtracking approach to get subsets
2. Get min and max of subset
3. Add min and max and put them in Hashmap (or update the count)
4. repeat this process for all subsets
5. search for k in hashmap and return count of k

input: {1,2,3,4,5}

subsets: 
1, 2, 3, 4, 5, {1,2},{1,3}
k = 5

count = 5

{1, 4},{2,3} {1,2,4}, {1,2,3,4} {1,3,4}'''

def countSubsets(nums,k):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]>k:
                break
            if nums[i]+nums[j]==k:
                count += 2**((j-i-1) if j-i>1 else 0)
    print(count)
    return count

countSubsets([1,2,3,4,5], 5)




