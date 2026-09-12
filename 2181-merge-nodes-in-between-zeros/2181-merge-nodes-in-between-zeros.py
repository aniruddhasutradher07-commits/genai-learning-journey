# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        result = head
        total = 0

        while current:
            if current.val != 0:
                total += current.val
            else:
                result.next = ListNode(total)
                result = result.next
                total = 0

            current = current.next

        return head.next            