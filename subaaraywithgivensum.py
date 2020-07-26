def subArraySum(arr, sumi,n ):  
	for i in range(n): 
		curr_sum = arr[i]  
		j = i + 1
		while j <= n: 
			if curr_sum == sumi: 
				print ("Sum found between") 
				print("indexes % d and % d"%( i, j-1)) 
				return 1
			if curr_sum > sumi or j == n: 
				break
			curr_sum = curr_sum + arr[j] 
			j += 1
	print ("No subarray found") 
	return 0

arr=[1,2,3,7,5]
subArraySum(arr, 12, len(arr))