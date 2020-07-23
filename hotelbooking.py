def areBookingsPossible(arrival, departure, n, k): 

	ans = [] 
	# Create a common vector both arrivals 
	# and departures. 
	for i in range(0, n): 
		ans.append((arrival[i], 1)) 
		ans.append((departure[i], 0)) 

	# Sort the vector 
	ans.sort() 
	#[(1, 1), (2, 0), (3, 1), (5, 1), (6, 0), (8, 0)]

	curr_active, max_active = 0, 0
	for i in range(0, len(ans)): 
		# If new arrival, increment current 
		# guests count and update max active 
		# guests so far 
		if ans[i][1] == 1:
			curr_active += 1
			max_active = max(max_active, 
							curr_active) 

		# if a guest departs, decrement 
		# current guests count. 
		else: 
			curr_active -= 1

	# If max active guests at any instant 
	# were more than the available rooms, 
	# return false. Else return true. 
	return k >= max_active 

arrival = [1, 3, 5] 
departure = [2, 6, 8] 
n = len(arrival) 
k=3
if areBookingsPossible(arrival, 
					departure, n, k): 
	print("Yes") 
else: 
	print("No") 