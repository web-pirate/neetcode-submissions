# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        dummy = ListNode()
        current = dummy
        while temp1 or temp2:
            
            if temp1 == None:
                current.next = temp2
                temp2 = temp2.next
                current = current.next
            elif temp2 == None:
                current.next = temp1
                temp1 = temp1.next
                current = current.next
            elif temp1.val > temp2.val:
                current.next = temp2
                current = current.next
                temp2 = temp2.next
            else:
                current.next = temp1
                current = current.next
                temp1 = temp1.next
            print(current.val)
        return dummy.next
        