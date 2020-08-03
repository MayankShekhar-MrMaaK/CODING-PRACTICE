# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        res=[-99999]
        
        def solve(root, res):
            
            if root is None:
                return 0
            
            l = solve(root.left, res)
            r = solve(root.right, res)
            
            temp= 1+ max(l,r) #PASS ABOVE
            ans = max(temp, 1+l+r) #INCLUDE IN ANS
            res[0] = max(res[0], ans)
            
            return temp
        
        solve(root,res)
        return res[0] -1
    
##LEETCODE