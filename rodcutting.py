def rod(wt, n):
  for i in range(n+1):
    for j in range(wt+1):
      if w[i-1]>j:
        t[i][j]=t[i-1][j]
      else:
        t[i][j]=max((value[i-1]+t[i][j-w[i-1]]), (t[i-1][j]))
  return t[n][wt]

def submem(n,wt):
  #BASE CASE
  if n==0 or wt==0:
    return 0

  if k[n][wt] != -1:
    return k[n][wt]
  
  #CHOICE DIAGRAM
  if w[n-1] > wt:
    k[n][wt]= submem(n-1,wt)
    return k[n][wt]
  else:
    k[n][wt]= max((value[n-1]+submem( n, wt-w[n-1])) ,(submem(n-1,wt)))
    return k[n][wt]

value=[2,5,7,8]
w=[1,2,3,4]
wt=5
n=len(value)
k=[[-1 for j in range(wt+1)] for i in range(n+1)]
t=[[0 for j in range(wt+1)] for i in range(n+1)]
print(rod(wt,n))
print(submem(n,wt))


'''
|-------->length
|
|
|
^'
[size of array or the elements present in array]
FILLED WITH 0
'''