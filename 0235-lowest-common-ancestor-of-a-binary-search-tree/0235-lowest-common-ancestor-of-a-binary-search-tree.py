# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def LCA(root, p, q):

            if not root:
                return None

            if root == p or root == q:
                return root

            left = LCA(root.left, p, q)
            right = LCA(root.right, p, q)

            if left != None and right != None:
                return root

            if left != None:
                return left
            
            return right

        return LCA(root, p, q)
