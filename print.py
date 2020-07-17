def rev(word):
	c=0
	for i in range(2,word):
		b=True;
		for j in range(2,i):	
			if i%j==0:
				b=False
				break
		if b:
			c+=1
	return c
print(rev(12))