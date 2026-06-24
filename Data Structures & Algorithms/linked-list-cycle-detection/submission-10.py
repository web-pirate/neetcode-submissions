# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # seen = []
        # po = head
        slow = head
        fast = head
        while fast and fast.next:
            if fast is None:
                return False
            
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
            
        return False
            