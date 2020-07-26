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

i=[1, 4, 45, 6, 10, 8] 
oi=[]
out=[]
subset(i,oi)
sumi=22
outi=[]
for k in out:
	if sum(k)==sumi:
		outi.append(k)
print(outi)