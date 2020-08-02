def compute_min_refills(distance, tank, stops):
	fuel=tank
	count=0
	stops += [distance, distance]
	for i in range(len(stops)-1):
		if fuel<stops[i]:
			return -1
		if fuel<stops[i+1]:
			fuel=stops[i]+tank
			count+=1
	return count
print(compute_min_refills(200,250,[100,150]))

