def wave(arr):
	arr.sort()

	for i in range(0,len(arr)-2,2):
		arr[i], arr[i+1]= arr[i+1], arr[i]

	return arr

arr=[3, 6, 5, 10, 7, 20]
print(wave(arr))


'''
Sort an array in wave form

Given an unsorted array of integers, sort the array into a wave like array. An array ‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..
Input:  arr[] = {3, 6, 5, 10, 7, 20}
Output: arr[] = {6, 3, 10, 5, 20, 7} OR any other array that is in wave form
'''