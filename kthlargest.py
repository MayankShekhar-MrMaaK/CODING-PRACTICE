stack=[]
k=2
arr=[3,1,2,4]
for i in arr:
	if len(stack)==0:
		stack.append(i)
		print(stack)
		continue
	elif len(stack)>0 and stack[-1]>i:
		stack.append(i)
		print(stack)

	elif len(stack)>0 and stack[-1]<i:
		stack=[i]+stack
		print(stack)
		
	if len(stack)>k:
		temp=min(stack)
		stack.remove(temp)

print(min(stack))
print(stack)
#min heap