# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []

        result = []

        q = []
        q.append(root)

        while q:
            
            ans = []
            size = len(q)
            
            while size:

                element = q.pop(0)
                ans.append(element.val)

                if element.left:
                    q.append(element.left)

                if element.right:
                    q.append(element.right)

                size -= 1
            
            result.append(ans)
        
        return result
