class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        suml = 0
        sumr = sum(nums)

        for i,n in enumerate(nums):
            sumr -= n
            if suml == sumr:
                return i
            suml += n
        return -1

        