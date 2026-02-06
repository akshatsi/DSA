class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        
        temp = head
        while temp:
            next_element = temp.next
            copy = Node(temp.val)
            
            temp.next = copy
            copy.next = next_element
            
            temp = next_element
        
        temp = head
        while temp:
            copy = temp.next
            if temp.random:
                copy.random = temp.random.next
            temp = temp.next.next
        
        temp = head
        dummyNode = Node(-1)
        res = dummyNode
        
        while temp:
            copy = temp.next
            res.next = copy
            res = res.next
            
            temp.next = copy.next
            temp = temp.next
        
        return dummyNode.next