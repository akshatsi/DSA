class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head


        temp = head
        count = 1
        while temp.next:
            count += 1
            temp = temp.next

        k %= count
        if k == 0:
            return head

        temp.next = head
        new_start = head

        for i in range(count - k -1):
            new_start= new_start.next

        new_head = new_start.next
        new_start.next = None

        return new_head