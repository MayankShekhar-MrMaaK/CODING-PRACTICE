def first(arr, target):
  res=-1
  low,high=0,len(arr)-1
  while low<=high:
    mid=low+(high-low)//2
    if arr[mid]>target:
      high=mid-1
    elif arr[mid]<target:
      low=mid+1
    else:
      res=mid
      high=mid-1
  return res

def last(arr,target):
  res=-1
  low,high=0,len(arr)-1
  while low<=high:
    mid=low+(high-low)//2
    if arr[mid]>target:
      high=mid-1
    elif arr[mid]<target:
      low=mid+1
    else:
      res=mid
      low=mid+1
  return res

arr=[1,2,2,2,3,4]
res=-1
target=2
print(first(arr,target))
print(last(arr,target))