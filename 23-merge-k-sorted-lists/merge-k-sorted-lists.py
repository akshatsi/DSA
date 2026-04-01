# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''#brute force
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

        return dummy.next'''
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap,(node.val, i , node))

        
        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i , node.next))

        return dummy.next