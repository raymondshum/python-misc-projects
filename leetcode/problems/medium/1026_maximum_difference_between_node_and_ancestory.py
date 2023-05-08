class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Key point: Keep track of min and max values for each
        path and calculate difference at the end.

        Link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

        Method: Use DFS. Ancestor is just a predecessor node. Track
        min and max values for each pathway and calculate the
        difference at the end (running off the leaf node).

        Returns: int of the maximum difference between ancestors or
        0 if root is None.
        """
        def dfs(node: Optional[TreeNode], current_max: int, current_min: int) -> int:
            if not node:
                return current_max - current_min
            current_max = max(current_max, node.val)
            current_min = min(current_min, node.val)
            left = dfs(node.left, current_max, current_min)
            right = dfs(node.right, current_max, current_min)
            return max(left, right)
        
        if not root:
            return 0
        
        return dfs(root, root.val, root.val)