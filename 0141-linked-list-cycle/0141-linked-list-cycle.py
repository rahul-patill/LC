# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t = head
        h = head

        if(t == None or t.next == None):
            return False

        while(h!=None and h.next!=None):
            t = t.next
            h = h.next.next

            if(t == h):
                return True
        
        return False
