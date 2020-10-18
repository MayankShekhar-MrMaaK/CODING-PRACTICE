arr=[1,2,0,0,1,2,2]
pivot=1
low=0
high=len(arr)-1
i=0
while i<=high:
	if arr[i]<pivot:
		arr[i],arr[low]=arr[low],arr[i]
		low+=1
		i+=1
	elif arr[i]>pivot:
		arr[i],arr[high]=arr[high],arr[i]
		high-=1
	else:
		i+=1
print(arr)