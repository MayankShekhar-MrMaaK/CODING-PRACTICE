def top(x,y,m,n):
  k=[[0 for j in range(n+1)] for i in range(m+1)]
  maximum=0
  for i in range(1,m+1):
    for j in range(1,n+1):
      if x[i-1]==y[j-1]:
        k[i][j]= 1+ k[i-1][j-1]
        maximum=max(k[i][j], maximum)
      else:
        k[i][j]=0

  return maximum

x="abcdefz"
y="abcfghijxyz"
print(top(x,y,len(x), len(y)))