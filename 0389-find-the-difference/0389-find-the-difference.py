class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tSum = sum(ord(c) for c in t)
        sSum = sum(ord(c) for c in s)

        return chr(tSum - sSum)

        