from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)

        freq_list = list(freq.items())

        freq_list.sort(key = lambda item:item[1] ,reverse = True)
        freq_list = freq_list[:k]

        return [item[0] for item in freq_list] 


        