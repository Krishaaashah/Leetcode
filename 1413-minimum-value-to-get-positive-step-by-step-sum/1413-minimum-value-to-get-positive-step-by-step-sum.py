class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum, ans = 0,0
        for el in nums:
            sum += el
            ans = min(ans,sum)
        return -ans + 1