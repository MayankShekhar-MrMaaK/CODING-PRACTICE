def check(summ):
	for i in prime:
		if i==summ:
			return 1
	return 0

def g(stri, pos, summ, tight):
	if pos==len(stri):
		if check(summ) :
			return 1
		else:
			return 0

	elif dp[pos][summ][tight]!=-1:
		return dp[pos][summ][tight]

	elif tight==1:
		res=0
		for i in range(0,int(stri[pos])):
			if i==int(stri[pos]):
				res+=g(stri,pos+1,summ+i,1)
			else:
				res+=g(stri,pos+1,summ+i,0)
		dp[pos][summ][tight]=res
		return res

	else:
		res=0
		for i in range(0,9):
			res+=g(stri,pos+1,summ+i,0)
		dp[pos][summ][tight]=res
		return res

prime=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]
l=10
r =19
l=l-1
a=str(l)
b=str(r)
dp=[[[-1 for k in range(2)] for j in range(80)]for i in range(10)]
ans1=g(b,0,0,1)
dp=[[[-1 for k in range(2)] for j in range(80)]for i in range(10)]
ans2=g(a,0,0,1)

print(ans1-ans2)