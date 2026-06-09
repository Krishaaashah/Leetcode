class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # Array to store the minimum price to reach each airport
        prices = [float("inf")] * n
        prices[src] = 0

        # Run the loop K + 1 times (since K stops means at most K + 1 flights)
        for i in range(k + 1):
            # Create a copy of prices to avoid using updated prices from the CURRENT layer
            tempprice = prices[:]
            
            for s, d, p in flights:
                # If we haven't reached the source airport yet, skip this flight
                if prices[s] == float("inf"):
                    continue
                
                # Check if taking this flight is cheaper than what we found before
                if prices[s] + p < tempprice[d]:
                    tempprice[d] = prices[s] + p
            
            # Update main prices array after exploring this layer of flights
            prices = tempprice

        # If dst is still inf, it means we can't reach it within K stops
        return -1 if prices[dst] == float("inf") else prices[dst]