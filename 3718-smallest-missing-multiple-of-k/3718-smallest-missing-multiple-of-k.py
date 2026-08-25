class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = set(nums)

        cur = k

        while cur in seen:
            cur += k
        return cur 

        
        