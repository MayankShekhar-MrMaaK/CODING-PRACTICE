def subset(i,oi):
	if len(i)==0:
		if len(oi)==3:
			out.append(oi)
		return
		
	o1=oi.copy()
  o2=oi.copy()
  o2.append(i[0])
  i=i[1:]
  subset(i,o1)
  subset(i,o2)
  
i=[2, 5, 8, 4, 6, 11] 
oi=[]
out=[]
subset(i,oi)
outi=[]
for k in out:
  if sum(k)==24:
		outi.append(k)
print(outi)