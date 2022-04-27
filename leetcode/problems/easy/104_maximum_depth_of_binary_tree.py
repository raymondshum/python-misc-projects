from leetcode.data_structures.tree_node import TreeNode, bfs_print
from typing import Optional

class Solution:
    """Key Point: Use recursive DFS to get the max depth.
    
    Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
    
    Method: Recursive method. Starting at root, count each existing node until the 
    furthest node is reached. Each recursive method call will only return the
    highest current count (1 or 0). All counts return up through the call
    stack.
    
    Returns: 
        Int: Max depth of tree
    """
    def maxDepth(self, root: Optional[TreeNode], count: int = 0) -> int:
        if not root:
            return 0
        
        current_count = count + 1
        left_count = self.maxDepth(root.left, 0)
        right_count = self.maxDepth(root.right, 0)
        return current_count + max(left_count, right_count)