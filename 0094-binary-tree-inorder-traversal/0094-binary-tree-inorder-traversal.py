# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # this is using morris traversal
        # https://www.youtube.com/watch?v=Wq3ibaP4dJY

        result = []

        cur = root

        while cur:

            if cur.left == None:
                result.append(cur.val)
                cur = cur.right
            else:
                leftChild = cur.left

                while leftChild.right:
                    leftChild = leftChild.right
                
                leftChild.right = cur

                # incrementing curr to the left child
                temp = cur
                cur = cur.left
                temp.left = None
        
        return result

