# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        f=head
        k=head
        while f and f.next:
            f=f.next.next
            k=k.next
            if k==f:
                return 1
        return 0
        
        
