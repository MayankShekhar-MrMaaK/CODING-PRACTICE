
def stair(n):
	if n<=1:
		return n
	 
	ways= stair(n-1) + stair(n-2)
	return ways

n=4
print(stair(n+1))