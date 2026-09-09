class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = (len(str(n))-1) //3
        return l * (n + 1) - (1000 ** (l+1) - 1000) // 999      