def per(i,o):
  if i=="":
    print(o)
    return
  
  o1=o
  o2=o
  o1=o1+i[0].lower()
  o2=o2+i[0].upper()
  i=i[1:]
  per(i,o1)
  per(i,o2)

per("ab","")

'''
OUTPUT:
ab
aB
Ab
AB
'''