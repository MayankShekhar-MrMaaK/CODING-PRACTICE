#Count NUMBER OF SUBSET WITH GIVEN DIFFERENCE

arr=[3, 1, 4, 1, 5]
d=2
s= (d+sum(arr))//2
n=len(arr)
k=[[0 for i in range (s+1)] for j in range(n+1)]


for i in range(n+1):
  k[i][0]=1
for i in range(1,s+1):
  k[0][i]=0

for i in range(1,n+1):
  for j in range(1,s+1):

    if arr[i-1]> j:
      k[i][j]= k[i-1][j]
    else:
      k[i][j]= k[i-1][j-arr[i-1]] + k[i-1][j]



print("Given Array {}\nNumber of Subset with given difference {} is {}".format(arr,d,k[n][s]))


'''Here we have to find S2-S1 equal to given difference

So eq [1]-> s2-s1= difference
   eq [2]-> s2+s1 = Total SUM
   =>eq[1] + eq[2]
   2s2= difference + Total SUM
   s2 = (difference + Total SUM)/ 2
   
   Hence s2 can be found i.e the required SUM'''