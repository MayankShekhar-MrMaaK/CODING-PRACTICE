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