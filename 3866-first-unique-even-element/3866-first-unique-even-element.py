class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for i in nums:
            if i % 2 == 0 and hashmap[i] == 1:
                return i
        return -1
        