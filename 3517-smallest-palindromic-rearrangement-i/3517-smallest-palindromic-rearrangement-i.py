class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) <= 2: return s

        cnt = Counter(s)
        left = []
        middle = ""

        for ch in sorted(cnt):
            left.append(ch * (cnt[ch] // 2))
            if cnt[ch] % 2:
                middle = ch

        left = "".join(left)
        return left + middle + left[::-1]