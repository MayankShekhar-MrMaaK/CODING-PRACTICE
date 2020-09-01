import heapq
def findsthLargest(nums, k):
	heap = []
	heapq.heapify(heap)
	for i in range(len(nums)):
		heapq.heappush(heap,nums[i])

	res=[]
	res.append([y for y in heapq.nsmallest(k, heap)])
	print(res)
	return res[-1][-1]

print(findsthLargest([5,2,3,1,9],4))