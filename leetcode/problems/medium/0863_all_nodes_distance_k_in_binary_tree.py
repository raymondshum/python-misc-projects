from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Key Point: Transform binary tree into undirected graph and then use BFS
        to find nodes K distance away.

        Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

        Method: Convert tree to undirected graph using DFS. Do so by drawing an
        edge between each node an its parent (allows backtracking). Then from the
        target node, use BFS to find all nodes K distance away. Track visited
        nodes to prevent cycles. Each level of BFS shows all nodes LEVEL distance
        away.

        Returns: List containing the int values of all nodes K distance away from
        the target node.
        """
        visited:          Set[TreeNode]   = {target}
        queue:            Deque[TreeNode] = deque([target])
        current_distance: int             = 0

        def dfs_convert_tree_to_undirected_graph(node: TreeNode, parent: TreeNode) -> None:
            if not node:
                return
            node.parent = parent
            dfs_convert_tree_to_undirected_graph(node.left, node)
            dfs_convert_tree_to_undirected_graph(node.right, node)
        
        dfs_convert_tree_to_undirected_graph(root, None)

        while queue and current_distance < k:
            num_nodes_in_level: int = len(queue)
            for _ in range(num_nodes_in_level):
                node: TreeNode = queue.popleft()
                for neighbor in [node.parent, node.left, node.right]:
                    if neighbor in visited or not neighbor:
                        continue
                    visited.add(neighbor)
                    queue.append(neighbor)
            current_distance += 1
        return [node.val for node in queue]