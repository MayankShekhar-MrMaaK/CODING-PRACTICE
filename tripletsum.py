def triplet(arr,n):
	ans=0
	for i in range(1, n-1):
		maxl=0
		maxr=0

		for j in range(0, i):
			if arr[i] > arr[j]:
				maxl=max(maxl, arr[j])

		for j in range(i+1, n):
			if arr[i] < arr[j]:
				maxr=max(maxr, arr[j])

		if maxl and maxr:
			ans= max(ans, maxl+arr[i]+maxr)
		
	return ans

arr=[2,5,3,1,4,9]
print(triplet(arr, len(arr)))

'''
 Instead of traversing through every triplets with three nested loops, we can traverse through two nested loops. While traversing through each number(assume as middle element(aj)), find maximum number(ai) smaller than aj preceding it and maximum number(ak) greater than aj beyond it. Now after that, update the maximum answer with calculated sum of ai + aj + ak
'''