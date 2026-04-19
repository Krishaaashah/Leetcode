class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return counter(s) == counter(t)

        