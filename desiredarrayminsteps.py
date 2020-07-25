def desired(arr,c):
	sumi=sum(arr)
	c=0
	while sumi!=0:
		if alleven(arr):
			c+=divide(arr)
		else:
			c+=substract(arr)

		sumi=sum(arr)
	return c

def alleven(arr):
	all=False
	for i in range(0,len(arr)):
		if arr[i]%2==0:
			all=True
		else:
			all=False
			break
	return all

def divide(arr):
	for i in range(0, len(arr)):
		arr[i]//=2
	return 1
	
def substract(arr):
	t=0
	for i in range(0,len(arr)):
		if arr[i]%2==0:
			pass
		else:
			arr[i]-=1
			t+=1
	return t
			
c=0
arr=[2,1]
print(desired(arr,c))