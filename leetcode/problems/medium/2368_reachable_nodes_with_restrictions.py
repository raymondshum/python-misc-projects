from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        """
        Key Point: Use DFS to explore the part of the graph 
        not blocked by restricted nodes.

        Link: https://leetcode.com/problems/reachable-nodes-with-restrictions/

        Method: Generate adjacency list from input Use DFS 
        to explore the graph. Track visited nodes and (the 
        set of) restricted nodes. Do not visit previously
        visited nodes or restricted nodes. Return number of
        nodes visited (will naturally be the max number).

        Returns: Int representing the maximum number of non
        restricted nodes that can be visited from the root.
        """
        ROOT_NODE:      int                  = 0
        adjacency_list: Dict[int, List[int]] = defaultdict(list)
        restricted:     Set(int)             = set(restricted)
        visited:        Set(int)             = set()

        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)

        def dfs_explore(node: int) -> None:
            visited.add(node)
            for neighbor in adjacency_list[node]:
                if neighbor in visited \
                    or neighbor in restricted:
                    continue
                dfs_explore(neighbor)

        dfs_explore(ROOT_NODE)
        return (max_reachable_nodes := len(visited))
