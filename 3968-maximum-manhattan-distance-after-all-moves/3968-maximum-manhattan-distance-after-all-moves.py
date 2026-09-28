class Solution:
    def maxDistance(self, moves: str) -> int:
        distance = [0,0]
        count = 0
        for i in moves:
            if i == 'L': distance[0] -= 1
            if  i == 'R': distance[0] += 1
            if i == 'U': distance[1] += 1
            if i == 'D': distance[1] -= 1
            if i == '_': count += 1
        
        result = abs(0-distance[0]) + abs(0-distance[1]) + count
        return result 

        