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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1