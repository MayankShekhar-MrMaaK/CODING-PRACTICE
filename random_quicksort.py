import random
arr=[5,7,85,4,6,1,2,9,3,4]
def quicksort(arr,l,r):
	if l >= r:
		return
	k = random.randint(l, r)
	arr[l], arr[k] = arr[k], arr[l]
	j, m = partition(arr, l, r)
	quicksort(arr,l,j-m)
	quicksort(arr,j+1,r)
def partition(arr,l,r):
	pivot = arr[l]
	j,k,m=l,1,0
	for i in range(l + 1, r + 1):
		if arr[i] < pivot:
			j += 1
			arr[i], arr[j] = arr[j], arr[i]
		elif arr[i] == pivot:
			j += 1
			arr[i], arr[j] = arr[j], arr[i]
			arr[j], arr[l + k] = arr[l + k], arr[j]
			k += 1
	while m < k:
		arr[l + m], arr[j - m] = arr[j - m], arr[l + m]
		m += 1
	return j, m
quicksort(arr,0,len(arr)-1)
print(arr)