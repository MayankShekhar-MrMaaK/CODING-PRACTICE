def reverses(arr,n):
  if n==1:
    return

  reverses(arr,n-1)
  last=arr[n-1]
  j=n-2

  while j>=0:
    arr[j+1]=arr[j]
    j-=1
  arr[j+1]=last

arr=[1,2,3,4,5]
print("orignal array-->{}".format(arr))
reverses(arr, len(arr))
print("reversed array-->{}".format(arr))