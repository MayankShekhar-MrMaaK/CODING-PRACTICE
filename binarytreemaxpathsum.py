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