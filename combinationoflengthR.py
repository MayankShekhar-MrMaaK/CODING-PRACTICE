startindex, bufferindex= 0, 0
arr=[1,2,3,4,5]
r=2
out=[0]*r

def combination(startindex, arr, bufferindex, out):
  #BaseCase
  if bufferindex==r:
    print(out)
    return

  for i in range(startindex, len(arr)): #BACKTRACKING
    out[bufferindex]=arr[i]
    combination(i+1, arr, bufferindex+1, out)

combination(startindex, arr, bufferindex,out)

'''
from itertools import combinations
lst = [1,2,3,4,5]
lengthOfStrings = 3
for i in combinations(lst, lengthOfStrings):
  print(i)
'''