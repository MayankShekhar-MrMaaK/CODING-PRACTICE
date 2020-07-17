arr=[1,20,6,4,5]
def merge_sort(arr,n):
	temp=[0]*n
	return mergesort(arr,temp,0,len(arr)-1)
def mergesort(arr,temp,left,right):				# MERGE SORT BASICS STEPS
	count=0
	if left<right:
		mid=(left+right)//2
		count+=mergesort(arr,temp,0,mid)		# LEFT SIDE ARRAY
		count+=mergesort(arr,temp,mid+1,right)	# RIGHT SIDE ARRAY
		count+=merge(arr,temp,left,mid,right)	# MERGING BOTH LEFT AND RIGHT ARRAY
	return count
def merge(arr,temp,l,mid,r):
	i=l 										# i for left array 
	j=mid+1 									# j for right array
	k=l 										# k for temp array
	count=0
	while i<=mid and j<=r: 						# Conditions are checked to make sure that i and j don't exceed their subarray limits.
		if arr[i]<=arr[j]: 						# NO INVERSION
			temp[k]=arr[i]						# just copying elements to temp
			i+=1
			k+=1
		else:									# INVERSION 
			temp[k]=arr[j]
			count+=mid-i+1						# In merge process, let i is used for indexing left sub-array and j for right sub-array.
												# At any step in merge(), if a[i] is greater than a[j], then there are (mid – i) inversions.
												# because left and right subarrays are sorted, so all the remaining elements in left-subarray
												# (a[i+1], a[i+2] … a[mid]) will be greater than a[j]
			j+=1
			k+=1
	while i<=mid:								# Copy the remaining elements of LEFT subarray into temporary array.
		temp[k]=arr[i]
		i+=1
		k+=1
	while j<=r:									# Copy the remaining elements of RIGHT subarray into temporary array.
		temp[k]=arr[j]
		j+=1
		k+=1
	for x in range(l, r + 1):					# Copy the elements of temp into arr.
		arr[x] = temp[x]
	return count
print(merge_sort(arr,len(arr)))