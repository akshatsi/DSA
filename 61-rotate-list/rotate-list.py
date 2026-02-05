class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head
        
        temp = head
        count = 1
        
        while temp.next:
            temp = temp.next
            count += 1
        
        k %= count
        if k == 0:
            return head
        
        temp.next = head  
        
        steps = count - k
        new_tail = head
        
        for _ in range(steps - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head