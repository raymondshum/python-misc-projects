from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        Key Point: Traverse the tree by level. Find the
        max value in every row.

        Link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/

        Method: Use BFS. Go level by level. At each level,
        keep track of the max value encountered. At each
        node, update the max value. At the end of each level,
        add the max value to the list of answers.

        Returns: The list of max node values per level or 
        an empty list if the root is None.
        """
        if not root:
            return []
        
        queue = deque([root])
        max_node_values_per_level = []

        while queue:

            num_nodes_in_current_level = len(queue)
            current_max = float(-inf)

            for _ in range(num_nodes_in_current_level):
                node = queue.popleft()
                current_max = max(current_max, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            max_node_values_per_level.append(current_max)
        
        return max_node_values_per_level