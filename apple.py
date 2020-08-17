def areConsecutive(m, n): 
	if ( n < 1 ): 
		return False 
	Min = min(m) 
	Max = max(m) 
	if (Max - Min + 1 == n): 
		visited = [False for i in range(n)] 
		for i in range(n): 
			if (visited[m[i] - Min] != False): 
				return False
			visited[m[i] - Min] = True
		return True
	return False 

def check():
	arr=[5,4,3,2,1]
	maxi=-999
	for i in range(len(arr)):
		curr=arr[i]
		res=0
		l=[]
		for j in range(len(arr)):
			temp=arr[j]
			if curr<= temp:
				res+=curr
				l.append(j)
		c=res

		if areConsecutive(l, len(l)):
			maxi=max(maxi, c)

	return maxi

print(check())