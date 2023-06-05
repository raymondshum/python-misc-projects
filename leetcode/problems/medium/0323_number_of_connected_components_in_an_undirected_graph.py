from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Key Point: Use DFS search and a hash set (seen) to track
        connected clusters or "islands" of nodes.

        Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

        Method: Build an adjacency list. Starting from first node,
        determine connected nodes using DFS. Add these nodes into
        seen. Count this is an "island". Move to next unseen node
        and repeat until no nodes remain.

        Returns: Int representing the number of "islands" or groups
        of connect nodes in a graph.
        """
        adjacency_list:     Dict[int, List[int]] = defaultdict(list)
        seen:               Set[int]             = set()
        num_connected:      int                  = 0
        disconnected_nodes: int                  = 0

        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)

        print(adjacency_list)
        
        def dfs_search(node: int):
            seen.add(node)
            for neighbor in adjacency_list[node]:
                if neighbor in seen:
                    continue
                dfs_search(neighbor)
        
        for node in adjacency_list:
            if node in seen:
                continue
            num_connected += 1
            dfs_search(node)

        disconnected_nodes = n - len(seen)
        return num_connected + disconnected_nodes