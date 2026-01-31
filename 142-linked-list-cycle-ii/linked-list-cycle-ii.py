# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''temp = head
        arr = []
        while temp:
            if temp in arr:
                return temp
            else:
                arr.append(temp)
            temp = temp.next
        return None'''
        slow = head
        fast = head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow
        return None