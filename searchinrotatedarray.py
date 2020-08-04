class Solution:
    def search(self, arr: List[int], target: int) -> int:
        
        if len(arr)==0 or arr==None:
            return -1
        
        left=0
        right=len(arr)-1
        minindex=0
        
        def minimum_element_index(left, right, arr):
            if len(arr)==0:
                return -1
            if len(arr)==1:
                return 0
            while left<= right:
                mid=left+(right-left)//2
                if mid> 0 and arr[mid]< arr[mid-1]:
                    return mid
                elif arr[mid]>= arr[left] and arr[mid]> arr[right]:
                    left=mid+1
                else:
                    right=mid-1
            return left
        
        minindex=minimum_element_index(left, right, arr)#RETURN MINIMUM ELEMENT's INDEX
        left=0
        right=len(arr)-1
        
        if target>= arr[minindex] and target<= arr[right]:
            left=minindex
        else:
            right=minindex
        
        while left<= right:  #NORMAL BINARY SEARCH
            mid=left+(right-left)//2
            if target == arr[mid]:
                return mid
            elif arr[mid]> target:
                right=mid-1
            else:
                left=mid+1
   
        return -1

#LEETCODE-->
'''
https://leetcode.com/problems/search-in-rotated-sorted-array/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''