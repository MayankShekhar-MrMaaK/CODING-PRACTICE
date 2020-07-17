def binarysearch(arr,low,high,x):
	if high<low:
		return -1

	mid=low+(high-low)//2

	if x==arr[mid]:
		return mid
	elif x<arr[mid]:
		return binarysearch(arr,low,mid-1,x)
	elif x>arr[mid]:
		return binarysearch(arr,mid+1,high,x)
    
arr=[1,5,8,12,13]
print(6," is at index ",binarysearch(arr,0,len(arr)-1,6))