"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # Created the hashmap
        oldtonew = {}

        # defined the depth forst f/n
        def dfs(node):
            #if node exits in the hashmap only return the return that node 
            if node in oldtonew:
                return oldtonew[node]

            # make a copy of node
            copy = Node(node.val)
            oldtonew[node] = copy

            #check for the neighbors 
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        return dfs(node) if node else None
        