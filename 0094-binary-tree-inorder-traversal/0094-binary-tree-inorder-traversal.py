# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative solution
        stack = []
        ans = []


        node = root

        while (True):
            # if node is not empty
            if (node != None):
                stack.append(node)
                node = node.left
            
            # if you got none at the leaf node
            else:
                if(len(stack) == 0):
                    break
                node = stack.pop()
                ans.append(node.val)
                node = node.right
        
        return ans
            

