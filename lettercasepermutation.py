def per(i,o,s):
  if i=="":
    s.add(o)
    return
  
  o1=o
  o2=o
  o1=o1+i[0].lower()
  o2=o2+i[0].upper()
  i=i[1:]
  per(i,o1,s)
  per(i,o2,s)

s=set()
per("a1B2","",s)
print(s)

'''
OUTPUT:-
A1b2
a1B2
A1B2
a1b2
'''