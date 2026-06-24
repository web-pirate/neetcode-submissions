# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        po = head
        while po:
            if po.next == None:
                return False
            elif po.val in seen:
                return True
            else:
                seen.append(po.val)
                po = po.next
        return False
            