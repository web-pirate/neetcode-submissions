# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        while l1 or l2:
            num1 = num1 * 10 +  l1.val if l1 else num1
            if l1:
                l1 = l1.next
            num2 = num2 * 10 + l2.val if l2 else num2
            if l2:
                l2 = l2.next
        s = int(str(num1)[::-1]) + int(str(num2)[::-1])
        print(int(str(num2)[::-1]))
        print(s)
        rs = str(s)[::-1]
        print(rs)
        # print(rs)
        dummy = ListNode()
        current = dummy
        for i in rs:
            current.next = ListNode(int(i))
            current = current.next
        return dummy.next
        