class Node():
	def __init__(self, data, left=None, right= None):
		self.left= left
		self.right=right
		self.data=data

def ctree(preorder, dict,start, end, pindex ):
	root= Node(preorder[pindex])
	pindex= pindex+1

	if pindex==len(preorder):
		return root, pindex
	
	index= dict.get(preorder[pindex])

	if start<= index and index + 1<= end - 1:
		root.left, pindex= ctree(preorder, dict, start, index, pindex)
		root.right, pindex= ctree(preorder, dict, index+1, end-1, pindex)

	return root, pindex

# Driver Code 
preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7]
postorder = [4, 5, 2, 8, 9, 6, 7, 3, 1]
dict={}
for i, e in enumerate(postorder):
	dict[e]=i
start=0
end=len(postorder)-1
pindex=0
root=ctree(preorder, dict,start, end, pindex )[0]

def inorder(root):
	if root:
		inorder(root.left)
		print(root.data)
		inorder(root.right)

inorder(root)