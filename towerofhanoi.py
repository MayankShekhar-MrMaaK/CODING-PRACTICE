def tower(n, s, d ,h):
  if n==1:
    print("Move disk 1 from {} to {}".format(s,d))
    return
  
  tower(n-1, s, h, d)
  print("Move disk {} from {} to {}".format(n,s,d))
  tower(n-1, h, d, s)

n=2
tower(n,'s','d','h')
