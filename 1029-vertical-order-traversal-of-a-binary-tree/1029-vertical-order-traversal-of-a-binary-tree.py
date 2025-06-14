# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # for storing the nodes in [col, row, values]
        nodes = []

        def traverse(node, row, col):
            if not node : return

            nodes.append([col, row, node.val])

            traverse(node.left, row+1, col-1)
            traverse(node.right, row+1, col+1)

        traverse(root, 0, 0)
        
        # sorting as per the values[col, row, values]
        nodes.sort()

        result = defaultdict(list)
        for col, row, val in nodes:
            result[col].append(val)
        
        
        return list(result.values())



        




