def floor(arr, target):
  res=-1
  low,high=0,len(arr)-1
  while low<=high:
    mid=low+(high-low)//2
    if arr[mid]>target:
      high=mid-1
    elif arr[mid]<target:
      low=mid+1
      res=arr[mid]
    else:
      return arr[mid]
  return res

def ceil(arr,target):
  res=-1
  low,high=0,len(arr)-1
  while low<=high:
    mid=low+(high-low)//2
    if arr[mid]>target:
      high=mid-1
      res=arr[mid]
    elif arr[mid]<target:
      low=mid+1
    else:
      return arr[mid]
  return res

arr=[10,20,30,40]
target=25
f=floor(arr,target)
c=ceil(arr,target)
if target-f < c-target:
  print(f)
else:
  print(c)