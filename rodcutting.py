def rod(wt, price, n):
  for i in range(len(price)+1):
    for j in range(n+1):
      if wt[i-1]>j:
        t[i][j]=t[i-1][j]
      else:
        t[i][j]=max((price[i-1]+t[i][j-wt[i-1]]), (t[i-1][j]))
  return t[len(price)][n]

price=[2,5,7,8]
wt=[1,2,3,4]
n=5
t=[[0 for j in range(n+1)] for i in range(len(price)+1)]
print(rod(wt,price,n))


'''
|-------->length
|
|
|
^'
[size of array or the elements present in array]
FILLED WITH 0
'''