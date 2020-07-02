def coin(arr,s):
  n=len(arr)

  k=[[0 for i in range(s+1)] for j in range(n+1)]

  for i in range(1,s+1):
    k[0][i]=0
  for i in range(n+1):
    k[i][0]=1

  for i in range(1,n+1):
    for j in range(1,s+1):
      if arr[i-1]> j:
        k[i][j]=k[i-1][j]
      else:
        k[i][j]= k[i][j-arr[i-1]] + k[i-1][j]
  
  return k[n][s]

arr=[1,2,3]
s=5
if s<0:
  print("NOT POSSIBLE")
else:
  print("There are {} max ways to get sum= {} from coins={}".format(coin(arr,s),s,arr))