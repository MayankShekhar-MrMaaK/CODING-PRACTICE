# Data structure to store a Binary Tree node
class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


# Recursive function to perform inorder traversal of a binary tree
def inorder(root):

	if root is None:
		return

	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)


# A recursive function to construct a full binary tree from given preorder
# and postorder sequence
def buildTree(preorder, pIndex, start, end, dict):

	# Consider the next item from the given preorder sequence
	# This item would be the root node of subtree formed by
	# the postorder[start, end] and increment pIndex
	root = Node(preorder[pIndex])
	pIndex = pIndex + 1

	# return if all keys are processed
	if pIndex == len(preorder):
		return root, pIndex

	# find the index of next key in postorder sequence to determine the
	# boundary of left and right subtree of current root node
	index = dict.get(preorder[pIndex])

	# fill the left and right subtree together
	if start <= index and index + 1 <= end - 1:
		# build the left subtree
		root.left, pIndex = buildTree(preorder, pIndex, start, index, dict)

		# build the right subtree
		root.right, pIndex = buildTree(preorder, pIndex, index + 1, end - 1, dict)

	return root, pIndex


# Construct a full binary tree from preorder and postorder sequence
def buildBinaryTree(preorder, postorder):

	# dict is used to efficiently find index of any element in given
	# postorder sequence
	dict = {}
	for i, e in enumerate(postorder):
		dict[e] = i

	# pIndex stores index of next node in the preorder sequence
	pIndex = 0

	# set range [start, end] for subtree formed by postorder sequence
	start = 0
	end = len(preorder) - 1

	# construct the binary tree and return it
	return buildTree(preorder, pIndex, start, end, dict)[0]


preorder = [1, 2, 4, 5, 3, 6, 8, 9, 7]
postorder = [4, 5, 2, 8, 9, 6, 7, 3, 1]

root = buildBinaryTree(preorder, postorder)

print("Inorder Traversal: ", end='')
inorder(root)