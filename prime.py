'''find all the prime number till N'''
import math
n=30
arr=[1]*(n+1)
i=2
while i*i<=n:
	if arr[i]==1:
		for j in range((i*i),n+1,i):
			arr[j]=0
	i+=1
count=0
for i in arr:
	if i==1:
		count+=1
print(arr)
print("Numbers of prime number in range",n,"is",count)