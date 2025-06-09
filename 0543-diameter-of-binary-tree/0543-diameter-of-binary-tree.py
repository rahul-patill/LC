# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def longestPath(root):
            if root == None:
                return 0

            l = longestPath(root.left)
            r = longestPath(root.right)

            self.diameter = max(l+r,self.diameter)

            return 1 + max(l,r)

        
        longestPath(root)
        return self.diameter