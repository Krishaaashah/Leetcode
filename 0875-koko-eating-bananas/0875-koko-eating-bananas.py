class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        while l < r:
            mid = (l+r) // 2
            total_hours = 0
            
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
            if total_hours <= h:
                r = mid
            else:
                l = mid + 1

        return l