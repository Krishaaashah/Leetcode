# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        prev = None

        idx = 0
        while idx < left - 1:
            curr = curr.next
            idx += 1
            
        before_reversed_section = curr
        tail_of_reversed_section = curr.next
        
        # Move pointers into the reversal section
        prev = None
        curr = curr.next
        idx += 1
        
        # Fix 3: Reverse using the index counter until reaching 'right'
        while idx <= right:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            idx += 1
            
        # Fix 4: Reconnect the reversed section back into the main list
        before_reversed_section.next = prev
        tail_of_reversed_section.next = curr
        
        return dummy.next
        
        