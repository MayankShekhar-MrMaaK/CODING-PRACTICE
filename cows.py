arr=[1,2,4,8,9,12,16]
n=len(arr)
c=4
low, high, best =arr[0], arr[n-1], 0
while (low<=high):
	mid=(low+high+1)/2
	left, cnt= 0, 1
	for (i,c) in zip(range(1,n), range(1,c)):
		if (arr[i]-arr[left])>=mid:
			left=i
			cnt+=1
	if cnt>= c:
		low=mid+1
		best=mid
	else:
		high=mid-1
print(int(best))