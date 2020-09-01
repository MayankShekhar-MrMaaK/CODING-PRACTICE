import heapq
points=[[3,3],[5,-1],[-2,4]]
K=2
heap = []
heapq.heapify(heap)
for i in range(len(points)):
		x = points[i][0]
		y = points[i][1]
		d = (x*x + y*y)
		heapq.heappush(heap,[d, [x, y]])
res = []
print(heap)

res.append([y for x, y in heapq.nsmallest(K, heap)])
out=[]
out=res.pop()
print(out)

#maxheap