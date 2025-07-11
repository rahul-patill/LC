# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {} #dict to store the parent

        # store the parent element in the dict
        def inOrderP(root):
            
            if not root:
                return
            
            if root.left:
                parent[root.left] = root
            inOrderP(root.left)

            if root.right:
                parent[root.right] = root
            inOrderP(root.right)


        def BFS(root, target, k):
            q = []
            q.append(target)

            visited = set()
            visited.add(target.val)

            while(q):
                n = len(q)

                if k == 0:
                    break
                
                for _ in range(n):
                    first = q.pop(0)

                    # left
                    if (first.left) and (first.left.val not in visited):
                        q.append(first.left)
                        visited.add(first.left.val)

                    # right
                    if (first.right) and (first.right.val not in visited):
                        q.append(first.right)
                        visited.add(first.right.val)
                    
                    # parent
                    # imp dict point here : why cant we use parent[first]?
                    if (parent.get(first)) and (parent[first].val not in visited):
                        q.append(parent[first])
                        visited.add(parent[first].val)
                    
                k -= 1

            result = []

            while q:
                result.append(q.pop(0).val)
            return result


            

        inOrderP(root)
        return BFS(root, target, k)
