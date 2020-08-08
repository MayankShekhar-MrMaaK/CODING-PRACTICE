def printpreorder(inorder, postorder, n): 
	if postorder[-1] in inorder: 
		root = inorder.index(postorder[-1])
	stack.append(postorder[-1])
		
	if root != 0: # left subtree exists 
		printpreorder(inorder[:root], 
					postorder[:root], 
					len(inorder[:root])) 
	
	if root != n - 1: # right subtree exists 
		printpreorder(inorder[root + 1:], 
					postorder[root: -1], 
					len(inorder[root + 1:])) 
		
# Driver Code 
postorder = [4, 12, 10, 18, 24, 22, 15, 31,44, 35, 66, 90, 70, 50, 25]
inorder = 	[4, 10, 12, 15, 18, 22, 24, 25,31, 35, 44, 50, 66, 70, 90]
n = len(inorder) 
stack=[]
printpreorder(inorder, postorder, n)
print ("Preorder traversal: {}".format(stack))
#25 15 10 4 12 22 18 24 50 35 31 44 70 66 90