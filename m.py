list=[]
s=20
arr=[3,2,2,3,4,6]
for k in range(1,5):
 for i in arr:
  list.append(i/k)
 total=sum(list)
 list=[]
 if total<s:
  break
print(k)
  