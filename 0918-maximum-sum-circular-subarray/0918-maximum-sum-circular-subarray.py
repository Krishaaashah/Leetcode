class Solution(object):
    def maxSubarraySumCircular(self, nums):
        total,maxsum,curmax,minsum, curmin = 0,nums[0],0,nums[0], 0 
        for a in nums:
            curmax = max(curmax + a, a)
            maxsum = max(maxsum,curmax)
            curmin = min(curmin+a,a)
            minsum = min(minsum,curmin)
            total += a
        return max(maxsum,total-minsum) if maxsum > 0 else maxsum
