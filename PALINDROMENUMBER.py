# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 21:04:30 2020

@author: MrMaak
"""
#12321 to check for palindrome to number
#best way is to convert it to string and then check it by #reversing.
def palin(num):
  snum=str(num)
  rnum=snum[::-1]
  return rnum==snum

# if conversion to string is not allowed then:
# using while loop [O[n]]
def palindrome(num):
    n=num
    rev=0
    while num>0:
        d = num % 10
        rev = rev * 10 + d
        num = num // 10
    return rev==n

# using Recursion
def recursion(num, rev=0):
    if num==0:
        return rev
    return recursion(num//10, rev*10+num%10 )
n=121
print("True" if recursion(n)==n else "False") 
    