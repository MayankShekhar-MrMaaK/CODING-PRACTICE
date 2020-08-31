stack=[]
k=4
out=[]
arr=[10, 9, 8, 7, 4, 70, 60, 50]
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
		out.append(temp)
#kth largest and min heap
print(stack)
print(out)