def reverse(arr):
  if len(arr)==1:
    return
  l=arr.pop(len(arr)-1)
  reverse(arr)
  insert(arr,l)

def insert(arr, element):
  if len(arr)==0:
    arr.append(element)
    return
  p=arr.pop(len(arr)-1)
  insert(arr,element)
  arr.append(p)

arr=[1,2,3,4,5]
print("orignal array-->{}".format(arr))
reverse(arr)
print("reversed array-->{}".format(arr))