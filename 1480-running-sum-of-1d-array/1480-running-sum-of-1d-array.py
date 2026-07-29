class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0

        num = []

        for i in range(len(nums)):
            num.append(sum+nums[i])

            sum += nums[i]

        return num
        