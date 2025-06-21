# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = []
        q.append((root, 0))
        maxW = 0

        while len(q) != 0:
            size = len(q)
            fSize = q[0][1]
            lSize = q[(len(q) - 1)][1]

            maxW = max(maxW, lSize - fSize + 1)

            while size:
                first = q[0][0]
                second = q[0][1]
                q.pop(0)

                if first.left:
                    q.append((first.left, ((2 * second) + 1)))
                if first.right:
                    q.append((first.right, ((2 * second) + 2)))

                size = size - 1

        return maxW