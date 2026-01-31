# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        arr = []
        while temp:
            if temp in arr:
                return True
            else:
                arr.append(temp)
            temp = temp.next
        return False

        