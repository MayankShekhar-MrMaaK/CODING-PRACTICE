arr=[3,4,0,0]
stack=[]
left=[]
#NEXT SMALLER TO LEFT
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
print("The maximum area possible in given gistogram is {}".format(max(out)))
maz=[]
matrix=[[1,2],[3,4]]
for u in matrix[0]:
	maz.append(u)
maz[0]=12
print(maz)
print(matrix)