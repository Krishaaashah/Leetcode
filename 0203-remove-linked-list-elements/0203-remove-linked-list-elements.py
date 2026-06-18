class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node pointing to head
        dummy = ListNode(-1)
        dummy.next = head
        
        # Use a pointer to traverse the list
        curr = dummy
        
        # Look ahead at the next node's value
        while curr.next:
            if curr.next.val == val:
                # Bypass the node to delete it
                curr.next = curr.next.next
            else:
                # Move forward only if we didn't delete a node
                curr = curr.next
                
        return dummy.next
