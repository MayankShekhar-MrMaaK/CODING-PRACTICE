# floor(log4(num))=ceil(log4(num) 

import math

def isPowerOfFour(n: int) -> bool:
	if n==0:
		return False
	return math.floor(math.log(n,4))==math.ceil(math.log(n,4))

print(isPowerOfFour(-2147483648))