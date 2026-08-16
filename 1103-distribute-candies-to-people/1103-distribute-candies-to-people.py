class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        give = 0

        while candies > 0:
            result[give % num_people] += min(candies, give + 1)
            give += 1
            candies -= give
        return result



        