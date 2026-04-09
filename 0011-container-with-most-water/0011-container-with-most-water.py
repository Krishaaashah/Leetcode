class Solution:
    def maxArea(self, height: List[int]) -> int:
        n =  len(height)
        l = 0
        r = n-1
        maxa = 0

        while l < r:
            w = r-l
            h = min(height[l],height[r])

            a = w*h

            maxa = max(maxa, a)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxa


        