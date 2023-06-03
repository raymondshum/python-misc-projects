class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Key Point: Return a list of nodes without incoming edges.

        Link: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

        Method: This only works for DAG. Otherwise, we'd have to
        worry about a cycle. So there would be no node that isn't
        reachable by any other node. We're finding only a list of 
        parents. They aren't reachable by any other nodes, so you 
        need to include each parent to reach every other node. 
        Initialize a list of size N to 0. Add 1 to list\[node\] for
        each incoming edge encountered. Return a list of nodes with
        no incoming edges.

        Returns: List of nodes with no incoming edges (parents).
        """
        indegrees: List[int] = [0] * n
        for _, destination_node in edges:
            indegrees[destination_node] += 1
        return [node for node, indegree in enumerate(indegrees) if indegree == 0]