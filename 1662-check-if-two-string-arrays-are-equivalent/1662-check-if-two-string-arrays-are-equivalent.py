class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        s1 = ""
        for w1 in word1:
            s1 += w1

        s2 = ""
        for w2 in word2:
            s2 += w2
        return s1 == s2 
        