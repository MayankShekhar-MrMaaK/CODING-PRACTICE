import heapq
arr=[1,1,1,2,2,3]
k=2
freq={}
for i in arr:
		if i in freq:
				freq[i]+=1
		else:
				freq[i]=1
arr=[]
for x,y in freq.items():
		arr.append([y,x])
heap = []
for i in range(len(arr)):
	heapq.heappush(heap,arr[i])
	if len(heap)>k:
		heapq.heappop(heap)
res = []
for i in range(k):
	res.append(heapq.heappop(heap)[1])
print(res)
print("dhd;")