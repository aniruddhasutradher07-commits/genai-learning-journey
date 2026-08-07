class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        left, right = head, prev
        result = True
        while right:  
            if left.val != right.val:
                result = False
                break
            left = left.next
            right = right.next
        curr = prev
        prev2 = None
        while curr:
            nxt = curr.next
            curr.next = prev2
            prev2 = curr
            curr = nxt

        return result