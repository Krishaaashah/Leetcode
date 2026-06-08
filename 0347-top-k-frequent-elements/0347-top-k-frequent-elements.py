from collections import Counter
class Solution:
    
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Will make the fequency of the given nums
        mapp = Counter(nums)

        #will convert the hashmap into the list
        m = list(mapp.items())


        # Now will sort the things in reverse order according to value of each key
        m.sort(key = lambda item: item[1], reverse=True)

        #make the answer list which is l in which appendded element till k
        l = m[:k]

        #will return the only key of frequenscies
        return [item[0] for item in l]

        

    

        