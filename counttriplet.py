def triplet(arr,n):
	total=0
	for i in range(1, n-1):
		lc=0
		rc=0
		for j in range(0,i):
			if arr[i]> arr[j]:
				lc+=1

		for j in range(i+1,n):
			if arr[i]< arr[j]:
				rc+=1

		total+=lc*rc
	
	return total

arr=[1,3,2]
print(triplet(arr, len(arr)))