stack=[]# storing index value
nums=[13,7,6,12,10]
stack.append(0)
out=[0 for i in range(len(nums))]

for i in range(len(nums)):  
	if len(stack)==0:
		stack.append(i)
		continue
	
	while len(stack)!=0 and nums[stack[-1]]< nums[i]:
		out[stack[-1]]=nums[i]
		stack.pop()
		
	stack.append(i)
	
for s in stack:
	out[s]=-1
	
print(out)