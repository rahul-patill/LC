# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        self.value = 0
        parent = defaultdict(lambda: None)
        
        def sumE(root):
            
            if not root:
                return

            # set root as parent for left and right child ,if exists
            if root.left:
                parent[root.left] = root
            if root.right:
                parent[root.right] = root

            # Check grandparent
            p = parent.get(root)
            gp = parent.get(p)
            if gp and gp.val % 2 == 0:
                self.value += root.val
            
            sumE(root.left)
            sumE(root.right)



        
        sumE(root)
        return self.value