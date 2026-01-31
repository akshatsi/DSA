class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return True

        # Step 1: find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        second_half = self.reverseList(slow)

        # Step 3: compare halves
        first = head
        second = second_half

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True