def sub(x,y,m,n):
  #BASE CONDITION
  if m==0 or n==0:
    return 0
  
  #memorization
  if t[m][n]!=-1:
    return t[m][n]
  #CHOICE DIAGRAM
  if x[m-1]==y[n-1]:
    t[m][n]= 1+ sub(x,y,m-1,n-1)
    return t[m][n]
  else:
    t[m][n]=max(sub(x,y,m-1,n), sub(x,y,m,n-1))
    return t[m][n]

def top(x,y,m,n):
  k=[[0 for j in range(n+1)] for i in range(m+1)]

  for i in range(1,m+1):
    for j in range(1,n+1):
      if x[i-1]==y[j-1]:
        k[i][j]= 1+ k[i-1][j-1]
      else:
        k[i][j]=max(k[i-1][j], k[i][j-1])

  return k[m][n]

x="abcdefz"
y="abcfghijxyz"
t=[[-1 for j in range(len(y)+1)] for i in range(len(x)+1)]
print(sub(x,y,len(x), len(y)))
print(top(x,y,len(x), len(y)))