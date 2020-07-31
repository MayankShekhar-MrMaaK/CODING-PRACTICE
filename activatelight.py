def activate(arr):



	n=len(arr)
	i=0
	while(i<=n-1):
		try:
			if arr[i]==0:
				i+=1
			
			if arr[i]==1:
				arr[i-2]=1
				arr[i-1]=1
				arr[i+1]=1
				arr[i+2]=1
				i+=3
		
		except IndexError:
			pass

	if sum(arr)==n-1:



'''
Problem Description

There is a corridor in a Jail which is N units long. Given an array A of size N. The ith index of this array is 0 if the light at ith position is faulty otherwise it is 1.

All the lights are of specific power B which if is placed at position X, it can light the corridor from [ X-B+1, X+B-1].

Initially all lights are off.

Return the minimum number of lights to be turned ON to light the whole corridor or -1 if the whole corridor cannot be lighted.
'''
		