def delete(k):
  
  if k==0:
    s.pop()
    return
  
  temp=s.pop()
  delete(k-1)
  s.append(temp)

s = [1,2,3,4,5] 
s1=s.copy()

k= len(s)//2-1 if len(s)%2==0 else len(s)//2 
delete(k)

print("The resultant stack after removing middle element from {} is {}".format(s1,s))