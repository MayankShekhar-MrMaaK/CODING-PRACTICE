def isPowerOfFour(n: int) -> bool:
	if n==1:
		return True
	
	if n>0 and n%4==0:
		n//=4
		return isPowerOfFour(n)

print(isPowerOfFour(36)==True)