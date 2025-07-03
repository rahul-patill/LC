# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def solve(root, target):

            if root == None:
                return None

            if root.val == target.val:
                return root

            lCall = solve(root.left, target)
            rCall = solve(root.right, target)

            if lCall:
                return lCall
            else :
                return rCall

        

        return solve(cloned, target)