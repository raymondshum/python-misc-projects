from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Key Point: Use DFS to search the tree for the target
        node, starting at a given source node.

        Link: https://leetcode.com/problems/find-if-path-exists-in-graph/

        Method: Build an adjacency list from the input. Start
        at the source node, and start to visit all connected
        nodes using DFS. Break and return True if the 
        destination node is found.

        Returns: True if path exists from source node to 
        destination node or False if not.
        """
        visited: Set[int] = set()
        adjacency_list: Dict[List[int]] = defaultdict(list)

        for node_1, node_2 in edges:
            adjacency_list[node_1].append(node_2)
            adjacency_list[node_2].append(node_1)
            
        def dfs_find_path(node: int) -> bool:
            visited.add(node)
            found_target: bool = False
            if node == destination:
                return True
            for node in adjacency_list[node]:
                if node in visited:
                    continue
                found_target = found_target or dfs_find_path(node)
                if found_target:
                    break
            return found_target
        
        return dfs_find_path(source)