# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 00:32:47 2020

@author: MrMaak
"""
# Given two integers dividend and divisor, 
#divide two integers without using 
#multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero,
# which means losing its fractional part. 
#For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
# Note:

# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only 
#store integers within the 32-bit signed integer range:[−231,231 − 1].
# For the purpose of this problem, assume that your function 
#returns 231 − 1 when the division result overflows.

def divison(dividend, divisor):
    neg = (dividend< 0) != (divisor<0)
    dividend= abs(dividend)
    divisor = div = abs(divisor)
    ans, count = 0, 1
    while dividend >= divisor :
        dividend-= div
        div+= div
        ans+= count
        count+= count
        if dividend < div:
            div=divisor
            count=1
    if neg:
        return max(-ans, -2147483648)
    else:
        return min(ans, 2147483648)
    

print(divison(10, 3))
