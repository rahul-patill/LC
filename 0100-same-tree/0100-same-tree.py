# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = []
        queue.append(p)
        queue.append(q)

        while len(queue) != 0:
            first = queue.pop(0)
            second = queue.pop(0)

            if (first == None) and (second == None):
                continue
            elif (first == None) or (second == None) or (first.val != second.val):
                return False

            queue.append(first.left)
            queue.append(second.left)
            queue.append(first.right)
            queue.append(second.right)
        
        return True
