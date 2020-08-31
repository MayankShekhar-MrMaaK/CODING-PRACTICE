def mah(arr):
	stack=[]
	left=[]
	for i in range(len(arr)):
		if len(stack)==0:
				left.append(-1)
		elif len(stack)>0 and stack[-1][0]<arr[i]:
				left.append(stack[-1][1])
		elif len(stack)>0 and stack[-1][0]>=arr[i]:
				while len(stack)>0 and stack[-1][0]>=arr[i]:
						stack.pop()
				if len(stack)==0:
						left.append(-1)
				else:
						left.append(stack[-1][1])
		stack.append([arr[i],i])
	stack=[]
	right=[]
	#NEXT SMALLER TO RIGHT
	for i in range(len(arr)-1,-1,-1):
		if len(stack)==0:
				right.append(len(arr))
		elif len(stack)>0 and stack[-1][0]<arr[i]:
				right.append(stack[-1][1])
		elif len(stack)>0 and stack[-1][0]>=arr[i]:
				while len(stack)>0 and stack[-1][0]>=arr[i]:
						stack.pop()
				if len(stack)==0:
						right.append(len(arr))
				else:
						right.append(stack[-1][1])
		stack.append([arr[i],i])
	right=right[::-1]

	out=[0] *len(arr)
	for i in range(len(arr)):
		out[i]=(right[i]-left[i]-1)*arr[i]
	return max(out)

matrix=[[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]
maz=[]
for u in matrix[0]:
	maz.append(u)
maxi=mah(maz)
for i in range(1,len(matrix)):
	for j in range(len(matrix[i])):
		if matrix[i][j]==0:
			maz[j]=0
		else:
			maz[j]=maz[j]+matrix[i][j]
	maxi=max(maxi, mah(maz))

print(maxi)