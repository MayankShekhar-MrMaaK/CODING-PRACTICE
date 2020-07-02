n=2
k=[[0 for i in range(n+1)] for j in range(n+1)]

for i in range(1,n+1):
  k[0][i]=0
for i in range(n+1):
  k[i][0]=1
    
for i in range(1,n+1):
  for j in range(1,n+1):
    if i > j:
      k[i][j]=k[i-1][j]
    else:
      k[i][j]= max(i * k[i][j-i] , k[i-1][j])

print(k)
print(k[n-1][n]) 
#demo file