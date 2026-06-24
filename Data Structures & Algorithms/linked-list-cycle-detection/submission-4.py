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
            if po is None:
                return False
            elif po in seen:
                return True
            else:
                seen.append(po)
                po = po.next
        return False
            