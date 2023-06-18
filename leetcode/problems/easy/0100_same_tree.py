from typing import Optional
from leetcode.data_structures.tree_node import TreeNode
class Solution:
    """
    Key Point: Use DFS to traverse two trees at once,
    comparing each node.

    Link: https://leetcode.com/problems/same-tree

    Method: Use DFS to traverse the tree. Return
    False if the node values don't equal. Return
    True if both node1 and node2 are Null. You'll
    only get all True returns if all values are
    equal until you run off the edge of a leaf
    node.

    Returns: Boolean True if both trees are the
    same and False if not.
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            if (not node1 or not node2) \
                or node1.val != node2.val:
                return False
            return dfs(node1.left, node2.left) \
                and dfs(node1.right, node2.right)
        return dfs(p,q)