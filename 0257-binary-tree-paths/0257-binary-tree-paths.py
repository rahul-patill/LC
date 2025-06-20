# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def rtl(root, ans):

            if not root.left and not root.right:
                ans = ans + [str(root.val)]
                paths.append("->".join(ans))
                return

            if root.left:
                rtl(root.left, ans + [str(root.val)])
            if root.right:
                rtl(root.right, ans + [str(root.val)])

        paths = []
        ans = []
        rtl(root, ans)
        return paths
