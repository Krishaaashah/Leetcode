class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur_sum  = nums[0]

        for n in range(1,len(nums)):
            cur_sum = max(nums[n],cur_sum + nums[n])

            res = max(res,cur_sum)
        
        return res




        