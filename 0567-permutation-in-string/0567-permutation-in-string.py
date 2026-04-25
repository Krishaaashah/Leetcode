class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        chars = [0] * 26
        defChars = [0] * 26
        for char in s1:
            defChars[ord(char) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            if r - l + 1 < len(s1):
                chars[ord(s2[r]) - ord('a')] += 1
                continue
            
            chars[ord(s2[r]) - ord('a')] += 1

            if chars == defChars:
                return True

            chars[ord(s2[l]) - ord('a')] -= 1
            l += 1
            
        return False