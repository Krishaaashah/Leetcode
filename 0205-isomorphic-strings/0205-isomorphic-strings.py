class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map = {}
        used_in_t = set() # Track characters already mapped in t
        
        for i in range(len(s)):
            if s[i] not in char_map:
                # If t[i] is already mapped to someone else, return False
                if t[i] in used_in_t:
                    return False
                char_map[s[i]] = t[i]
                used_in_t.add(t[i])
            elif char_map[s[i]] != t[i]:
                return False
                
        return True







        