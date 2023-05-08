from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Key Point: Return a forward or reversed list of
        node values, alternative per level of the tree.

        Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

        Method: Use BFS. Store a list of values per level
        of the tree. If the level is odd, add that list to
        the list of answers. If it is even, add the reversed
        list instead.

        Returns: List of node values in zig zag order or
        an empty list if the root is None.
        """
        if not root:
            return []
        
        queue = deque([root])
        zig_zagged_levels = []
        current_level = 1

        while queue:
            num_nodes_in_level = len(queue)
            current_node_values = []
            for _ in range(num_nodes_in_level):
                node = queue.popleft()
                current_node_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if current_level % 2 == 0:
                zig_zagged_levels.append(current_node_values[::-1])
            else:
                zig_zagged_levels.append(current_node_values)
            
            current_level += 1
        return zig_zagged_levels