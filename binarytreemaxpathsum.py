# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        res=[-9999]
        
        def solve(root, res):
            
            if root is None:
                return 0
            
            l= solve(root.left, res)
            r=solve(root.right, res)
            
            temp=max(max(l,r)+root.val , root.val)
            ans=max(temp, root.val+l+r)
            res[0] =max(res[0], ans)
            
            return temp
        
        solve(root, res)
        return res[0]

#LEETCODE
'''
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
'''