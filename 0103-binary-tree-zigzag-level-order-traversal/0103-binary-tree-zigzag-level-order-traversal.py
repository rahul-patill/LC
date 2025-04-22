# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root == None : return ans

        q = []
        q.append(root)

        flag = False

        while len(q) != 0:
            level = []
            stack = []
            size = len(q)

            for i in range(size):
                node  = q.pop(0)
                if flag:
                    stack.append(node.val)
                else:
                    level.append(node.val)

                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            flag = not flag  

            while len(stack) != 0:
                level.append(stack.pop())

            ans.append(level)

        return ans
