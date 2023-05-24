from typing import Set, List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Key Point: Use DFS and a hash set to track groups of 
        visited provinces.

        Link: https://leetcode.com/problems/number-of-provinces/

        Method: For each node, use DFS to visit all connected
        neighbors. Track each visited neighbor in a hash set.
        Record each group of connected nodes as a province.

        Returns: Number of groups of directly connected nodes.
        """
        def dfs(starting_node: int, edge_map: List[List[int]], visited_nodes: Set[int]):
            visited_nodes.add(starting_node)
            for neighbor, is_connected in enumerate(edge_map[starting_node]):
                if not is_connected or neighbor in visited_nodes:
                    continue
                dfs(neighbor, edge_map, visited_nodes)
                
        visited: Set[int] = set()
        num_provinces: int = 0
        for node in range(len(isConnected)):
            if node in visited:
                continue
            
            dfs(node, isConnected, visited)
            num_provinces += 1
        return num_provinces