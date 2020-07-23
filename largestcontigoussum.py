from sys import maxsize

def lcsum(arr):
	maxsumsofar= -maxsize-1
	maxendinghere=0

	for i in range(len(arr)):
		maxendinghere+=arr[i]

		if maxendinghere > maxsumsofar:
			maxsumsofar=maxendinghere

		if maxendinghere < 0:
			maxendinghere=0

	return maxsumsofar

def printlcsum(arr):
	maxsumsofar= -maxsize-1
	maxendinghere=0
	start,end=0,0
	s=0
	for i in range(len(arr)):
		maxendinghere+=arr[i]
		if maxendinghere > maxsumsofar:
			maxsumsofar=maxendinghere
			start=s
			end=i
		if maxendinghere < 0:
			maxendinghere=0
			s=i+1
	return maxsumsofar, start, end


arr= [-2, -3, 4, -1, -2, 1, 5, -3]
#[-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
print(lcsum(arr))
print(printlcsum(arr))


'''Largest Sum Contiguous Subarray

Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.
'''