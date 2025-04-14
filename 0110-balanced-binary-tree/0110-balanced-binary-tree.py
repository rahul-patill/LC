# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if root == None:
                return 0

            l = getHeight(root.left)
            r = getHeight(root.right)

            if (l == -1) or (r == -1):
                return -1

            if abs(l - r) > 1:
                return -1
            else:
                return abs(1 + max(l, r))
        
        ans = getHeight(root)
        return False if ans ==-1 else True 
