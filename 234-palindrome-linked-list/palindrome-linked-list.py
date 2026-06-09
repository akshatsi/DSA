# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse_list(head):
            temp = head
            prev = None

            while temp:
                front = temp.next
                temp.next = prev
                prev = temp 
                temp = front
            return prev

        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first = head
        second = reverse_list(slow)

        while second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True
        