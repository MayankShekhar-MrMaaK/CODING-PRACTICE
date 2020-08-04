def mySqrt(x: int) -> int:
		
		l=0
		r=x
		
		while l+1<r:
				mid= l+(r-l)//2
				
				sq=mid * mid
				if sq==x:
						return mid
				elif sq>x:
						r=mid
				else:
						l=mid
		
		if l*l ==x:
				return l
		elif r*r==x:
				return r
		else:
				return l

print(mySqrt(8))