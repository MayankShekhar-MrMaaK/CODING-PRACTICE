def leader(arr):
	out=[]
	n=len(arr)
	curr=arr[n-1]
	out.append(curr)

	for i in range(n-2, -1, -1):
		if arr[i]> curr:
			out.append(arr[i])
			curr=arr[i]
	
	return out

arr=[16, 17, 4, 3, 5, 2]
print(leader(arr))