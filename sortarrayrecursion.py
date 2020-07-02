def sorting(arr,n):
  #BASE CASE
  if n==1:
    return

  #INDUCTION
  sorting(arr,n-1)

  #HYPOTHETICAL
  last=arr[n-1]
  j=n-2
  
  while j>=0 and arr[j]>last :
    arr[j+1]=arr[j]
    j-=1
  arr[j+1]=last

arr=[5,1,7,3,5,-1]
print("orignal array-->{}".format(arr))
sorting(arr,len(arr))
print("sorted array-->{}".format(arr))