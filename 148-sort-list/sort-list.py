class Solution:

    def mergeTwoSortedLinkedLists(self, list1, list2):
        dummy = ListNode(-1)
        temp = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        if list1:
            temp.next = list1
        if list2:
            temp.next = list2

        return dummy.next

    def findMiddle(self, head):
        slow = head
        fast = head.next   # important for correct split

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sortList(self, head):
        if not head or not head.next:
            return head

        middle = self.findMiddle(head)
        right = middle.next
        middle.next = None

        left = self.sortList(head)
        right = self.sortList(right)

        return self.mergeTwoSortedLinkedLists(left, right)