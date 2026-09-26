class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        return sum(abs(x-y) for x, y in zip(sorted(seats), sorted(students)))

        