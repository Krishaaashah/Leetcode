class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxdepth = 0
        depth = 0

        for i in s:
            if i == "(":
                depth += 1
                maxdepth = max(maxdepth, depth)
            if i == ")":
                depth -= 1
                
        return maxdepth


             

        