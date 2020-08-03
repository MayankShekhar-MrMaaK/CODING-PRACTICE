class Node: 
    # Constructor to create a new node 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None

def maxPathSum(root) -> int:
	res=[-9999]
		
	def solve(root, res):
			
			if root is None:
					return 0
			
			l= solve(root.left, res)
			r=solve(root.right, res)
			
			temp=max(l,r)+root.val
			if root.left is None and root.right is None:
				temp=max(temp, root.val)

			ans=max(temp, root.val+l+r)
			res[0] =max(res[0], ans)
			
			return temp
	
	solve(root, res)
	return res[0]
    
# Driver program to test above function 
root = Node(-15) 
root.left = Node(5) 
root.right = Node(6) 
root.left.left = Node(-8) 
root.left.right = Node(1) 
root.left.left.left = Node(2) 
root.left.left.right = Node(6) 
root.right.left = Node(3) 
root.right.right = Node(9) 
root.right.right.right= Node(0) 
root.right.right.right.left = Node(4) 
root.right.right.right.right = Node(-1) 
root.right.right.right.right.left = Node(10) 
  
print ("Max pathSum of the given binary tree is{}".format( maxPathSum( root)))

'''
Given a binary tree in which each node element contains a number. Find the maximum possible sum from one leaf node to another.
The maximum sum path may or may not go through root. For example, in the following binary tree, the maximum sum is 27(3 + 6 + 9 + 0 – 1 + 10). Expected time complexity is O(n).
'''