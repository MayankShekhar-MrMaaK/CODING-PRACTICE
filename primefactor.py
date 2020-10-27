def isPrime(i):
  count=1
  for j in range(1,i//2+1):
    if i%j==0:
      count+=1
  if count==2:
    return 1
  return 0

def factor(num,arr):
  for i in range(1,num//2+1):
    if num%i==0 and isPrime(i):
      arr.append(i)

num=int(input("Enter a number...\n"))
arr=[]
factor(num, arr)
print(arr)