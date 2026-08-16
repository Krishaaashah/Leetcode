class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        check = list(stones)
        c = 0
        check2 = list(jewels)
        for i in check:
            if i in check2:
                c += 1
        return c

        