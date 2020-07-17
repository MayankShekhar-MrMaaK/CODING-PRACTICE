# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 02:01:02 2020

@author: MrMaak
"""


#Longest Common Prefix
# Write a function to find the longest common prefix string 
# amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

def longestCommonPrefix(strs):
    prefix = strs[0] if strs else ''
    while True:
        if all(s.startswith(prefix) for s in strs):
            return prefix
        prefix = prefix[:-1]
print(longestCommonPrefix(["flower","flow","flight"]))



