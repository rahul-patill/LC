# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        iOList = []

        def inOrder(root):
            if not root:
                return
            
            inOrder(root.left)
            iOList.append(root.val)
            inOrder(root.right)

        
        inOrder(root)

        isBst = True
        for i in range(1,len(iOList)):
            
            if iOList[i-1] >= iOList[i]:
                isBst = False
                break
        
        return isBst

