# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        k = []

        curr = head

        while curr:
            k.append(str(curr.val))
            curr = curr.next
        st = k[::-1] 

        total = 0
        # Complete your loop with an index to keep track of the power
        for i, ch in enumerate(st):
            if ch == "1":
                total += 2 ** i # Add 2 raised to the power of the position
                
        return total

        
        