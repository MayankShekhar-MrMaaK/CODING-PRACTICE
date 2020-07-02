'''
TARGET SUM --> https://leetcode.com/problems/target-sum/
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.'''

nums=[1,0]
S=1
def kaa(nums, S):

  c=0
  for i in nums:
    if i==0:
      c+=1
  
  if S > sum(nums):
    return 0;
  if (S+sum(nums))%2!=0 :
    return 0;

  s= (S+sum(nums))//2
  n=len(nums)

  k=[[0 for i in range (s+1)] for j in range(n+1)]
  for i in range(n+1):
    k[i][0]=1
  for i in range(1,s+1):
    k[0][i]=0

  for i in range(1,n+1):
    for j in range(1,s+1):
      if nums[i-1]==0:
        k[i][j] = k[i-1][j];
      elif nums[i-1]> j:
        k[i][j]= k[i-1][j]
      else:
        k[i][j]= k[i-1][j-nums[i-1]] + k[i-1][j]

  return 2**c * k[n][s];

print("Given Array {}\nNumber of Subset with -/+ given TOTAL SUM {} is {}".format(nums, S, kaa(nums, S)))


'''Basically we have to find 2 subset one for + and another for negative
so it is a Count number of subset with given difference problem.

Let us assume S as d and +ve_subset as s2 and -ve_subset as s1
Here we have to find S2-S1 equal to given difference i.e d

So eq [1]-> s2+(-s1)== s2-s1= d
eq [2]-> s2-(-s1)== s2+s1 = Total SUM
=>eq[1] + eq[2]
2s2= difference + Total SUM
s2 = (difference + Total SUM)/ 2

Hence s2 can be found i.e the required SUM'''