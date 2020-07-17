def per(i,o):
  if len(i)==1:
    print(o+i[0])
    return

  o1=o
  o2=o
  o1=o1+i[0]
  o2=o2+i[0]+"_"
  i=i[1:]
  per(i,o1)
  per(i,o2)

per("abc","")

'''OUTPUT:- 
abc
ab_c
a_bc
a_b_c
'''