def subset(i,o):
  if i=="":
    print(o)
    return
  
  o1=o
  o2=o
  o2=o2+i[0]
  i=i[1:]
  subset(i,o1)
  subset(i,o2)
  
i="abc"
o=""
subset(i,o)

'''
def subset(i,oi):
  if len(i)==0:
    print(oi)
    return
  
  o1=oi.copy()
  o2=oi.copy()
  o2.append(i[0])
  i=i[1:]
  subset(i,o1)
  subset(i,o2)
  
i=[1, 4, 9] 
oi=[]
out=[]
subset(i,oi)
'''