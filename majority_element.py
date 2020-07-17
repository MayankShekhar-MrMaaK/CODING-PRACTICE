def majority(arr,low,size):
	m={}
	for i in range(size):
		if arr[i] in m:
			m[arr[i]]+=1
		else:
			m[arr[i]]=1
	count=0
	for key in m:
		if m[key]>size//2:
			count=1
			break
	print(m)
	if count==1:
		return 1
	else:
		return 0
arr=[1,2,3,1]
size=len(arr)
print(majority(arr,0,size))