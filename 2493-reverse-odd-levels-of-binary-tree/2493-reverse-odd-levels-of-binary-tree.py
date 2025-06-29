# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        q = [] 
        q.append(root)

        flag = False
        #BFS start
        while q:
            size = len(q)

            # for each level
            while size:
                node = q.pop(0)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
                size -= 1
            
            flag = not flag
            
            #reversing values in q
            if flag:
                i = 0
                j = len(q)-1

                while i<j:
                    temp = q[i].val
                    q[i].val = q[j].val
                    q[j].val = temp
                    
                    i = i+1
                    j = j-1
            
        return root


