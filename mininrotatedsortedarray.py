class Solution:
    def findMin(self, arr: List[int]) -> int:
        if len(arr)==0:
            return -1
        if len(arr)==1:
            return arr[0]
        
        left=0
        right=len(arr)-1
        
        while(left<= right):
            mid= left+(right-left)//2
            
            if mid>0 and arr[mid]<arr[mid-1]:
                return arr[mid]
            
            elif arr[mid]>= arr[left] and arr[mid]> arr[right]:
                left= mid+1
                
            else:
                right=mid-1
                
        return arr[left]
