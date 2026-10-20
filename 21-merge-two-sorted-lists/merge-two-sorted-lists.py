class Solution:
    def mergeTwoLists(self, list1, list2):
        dummyNode = ListNode(-1)
        curr1 = list1
        curr2 = list2
        curr = dummyNode

        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next

            curr = curr.next

        curr.next = curr2 if curr1 is None else curr1
        return dummyNode.next