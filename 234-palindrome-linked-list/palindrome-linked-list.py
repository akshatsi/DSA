# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        prev = None
        original = []
        pall = []
        while temp:
            original.append(temp.val)
            front = temp.next
            temp.next = prev
            prev = temp 
            temp = front
        temp2 = prev
        while temp2:
            pall.append(temp2.val)
            temp2 = temp2.next
        if original == pall:
            return True
        else:
            return False