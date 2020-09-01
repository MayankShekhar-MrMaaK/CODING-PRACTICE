import heapq
def findKthLargest(nums, k):
	heap = []
	heapq.heapify(heap)
	for i in range(len(nums)):
		heapq.heappush(heap,nums[i])

	res=[]
	res.append([y for y in heapq.nlargest(k, heap)])
	print(res)
	return res[-1][-1]

print(findKthLargest([3,1,2,4],2))

#minheap