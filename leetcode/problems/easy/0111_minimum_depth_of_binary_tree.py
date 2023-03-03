from leetcode.data_structures.tree_node import TreeNode
from typing import Optional
import math
class Solution:
    """
    Keypoint: Used DFS to traverse all nodes. 

    Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/

    Method: Use DFS to reach each leaf node. Track the current depth
    of each level as you traverse down. Once you reach the leaf, return
    the values back up the stack. Keep the min of the left and right
    subtrees at each node.

    Returns: int of the minimum depth from root to a leaf node.
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root: Optional[TreeNode], current_depth:int) -> float:
            if not root.left and not root.right:
                return current_depth
            min_left: float = math.inf
            min_right: float = math.inf
            if root.left:
                min_left: float = dfs(root.left, current_depth + 1)
            if root.right:
                min_right: float = dfs(root.right, current_depth + 1)
            return min(min_left, min_right)
        return int(dfs(root, 1))
