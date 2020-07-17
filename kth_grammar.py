def grammar(n,k):
  if n==1 or k==1:
    return 0

  mid=(2**(n-1))//2

  if k<=mid:
    return int(grammar(n-1,k))
  else:
    return int(not(grammar(n-1,k-mid)))

print(grammar(3,3))


#0
#01
#0110
#01101001