stack=[]
k=4
arr=[7,10,4,3,20,15]
for i in arr:
	if len(stack)==0:
		stack.append(i)
		continue
	elif len(stack)>0 and stack[-1]<i:
		stack.append(i)
	elif len(stack)>0 and stack[-1]>i:
		stack=[i]+stack
	if len(stack)>k:
			stack.pop()

print(stack[-1])
print(stack)
#max heap