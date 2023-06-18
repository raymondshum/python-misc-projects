from typing import Optional
from leetcode.data_structures.tree_node import TreeNode
class Solution:
    """
    Key Point: Use DFS to traverse both left and right
    subtrees. Compare opposite children.

    Link: https://leetcode.com/problems/symmetric-tree/

    Method: This is similar to [same tree](#0100_same_treepy)
    except opposite children are compared.

    Returns: Bool True if left and right subtrees are
    mirror immages and False if not.
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if not node1 and not node2:
                return True
            if (not node1 or not node2) \
                or node1.val != node2.val:
                return False
            return dfs(node1.left, node2.right) \
                and dfs(node1.right, node2.left)
        return dfs(root.left, root.right)