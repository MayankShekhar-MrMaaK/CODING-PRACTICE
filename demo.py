
arrival = [1, 3, 5] 
departure = [2, 6, 8]
ans=[]
n=len(arrival)
for i in range(0, n): 
	ans.append((arrival[i], 1)) 
	ans.append((departure[i], 0))
[(1, 1), (2, 0), (3, 1), (5, 1), (6, 0), (8, 0)]
print(ans)