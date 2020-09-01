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
heapq.heapify(heap)
for i in range(len(arr)):
	heapq.heappush(heap,arr[i])

res = []
res.append([y for x, y in heapq.nlargest(k, heap)])

out=[]
out=res.pop()
print(out)

print("dhd;")