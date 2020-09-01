import heapq
def findKthLargest(nums, k):
	heap = []
	for i in range(len(nums)):
		heapq.heappush(heap,nums[i])
		if len(heap)>k:
			heapq.heappop(heap)

	print(heap)
	return heap[0]

print(findKthLargest([3,1,2,4],2))