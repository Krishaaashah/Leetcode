class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        l = sorted(list(set(nums)))
        
        
        countt = 1
        max_count = 1
        for i in range(len(l)-1):
            if l[i+1] == l[i] +1:
                countt  += 1
            
            else:
                #Reset counter to 1 if the chain breaks
                countt = 1
            max_count = max(countt,max_count)
        return max_count
    


        