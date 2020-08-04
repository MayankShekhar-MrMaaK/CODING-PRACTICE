def myPow(x: float, n: int) -> float:
		if n==0 :
				return 1
		else :
				if n>0 :
						return power(x,n)
				else :
						return 1/power(x,-n)
def power(x,n) :
		if n==0 :
				return 1
		temp=power(x,n//2)
		ans=temp*temp
		if n%2==0 :
				return ans
		else :
				return x*ans

print(myPow(2.1,3))