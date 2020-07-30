
n, k = [int(c) for c in input().split()]
l=[int(c) for c in input().split()]
p=[0]* n
print(l)
queries=[]
for _ in range(k):
  t = [int(c) for c in input().split()]
  queries.append(t)
	
def update(arr):
	p=[0]*len(arr)
	p[0]=arr[0]
	for i in range(1,len(arr)):
		p[i]=arr[i]+ p[i-1]

for i in queries:
	if i[0]==1:
		
		for j in range(i[1]-1, i[2]):
			if l[j]==0:
				l[j]=1
			else:
				l[j]==0
			update(l)
	else:
		summ=0
		for j in range(i[1]-1, i[2]):
			summ+=l[j]
		print(summ%(10^9 + 7))


'''Sample Input:
9 6
1 0 0 1 1 0 0 0 1
1 2 6
1 4 8
2 1 9
2 3 5
1 2 7
2 5 8

Sample Output:
41
12
8

Explanation:
Array P initially: [1, 1, 1, 2, 3, 3, 3, 3, 4]
After 1st query:
A: [1, 1, 1, 0, 0, 1, 0, 0, 1]
P: [1, 2, 3, 3, 3, 4, 4, 4, 5]
After 2nd query:
A: [1, 1, 1, 1, 1, 0, 1, 1, 1]
P: [1, 2, 3, 4, 5, 5, 6, 7, 8]
'''