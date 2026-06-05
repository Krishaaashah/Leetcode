# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        prev = head

        for _ in range(k-1):
            prev = prev.next
        
        left = prev
        right = head

        while prev.next:
            prev= prev.next
            right = right.next
        left.val,right.val = right.val, left.val
        return head