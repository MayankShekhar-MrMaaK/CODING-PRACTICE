def change(m):
	deno=[1,5,10]
	ans=[]
	i=len(deno)-1
	while(i >= 0):
		while(m>=deno[i]):
			m-=deno[i]
			ans.append(deno[i])
		i-=1
	print(ans)
	return len(ans)
print(change(23))
