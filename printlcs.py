def lcsp(m,n):
	for i in range(1,m+1):
		for j in range(1,n+1):
			if x[i-1]==y[j-1]:
				t[i][j] =1+t[i-1][j-1]
			else:
				t[i][j]=max(t[i-1][j], t[i][j-1])

x="abcdef"
y="acehgfhgk"
t=[[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
lcsp(len(x),len(y))

#PRINT
i, j=len(x),len(y)
s=""
while i>0 and j>0:
	if x[i-1]==y[j-1]:
		s+=x[i-1]
		i-=1
		j-=1
	else:
		if t[i][j-1]> t[i-1][j]:
			j-=1
		else:
			i-=1
s=s[-1::-1]
print(s)