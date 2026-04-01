# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #brute force
        all_results = []
        for head in lists:
            while head:
                all_results.append(head.val)
                head = head.next

        all_results.sort()
        dummy = ListNode(0)
        current = dummy

        for i in all_results:
            current.next = ListNode(i)
            current = current.next

        return dummy.next

