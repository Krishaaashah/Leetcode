class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxx = max(nums)
        minn = min(nums)
        r = []
        n_set = set(nums)

        for i in range(minn+1, maxx):
            if i not in n_set:
        
                r.append(i)
        return r
        