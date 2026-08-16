class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def get_next_number(n):
            output = 0

            while n  > 0:
                digit = n % 10
                output += digit ** 2
                n = n // 10

            return output
        slow = n
        fast = n
        while True:
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))

            if slow == fast:
                break
        return slow == 1
        