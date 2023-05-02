from typing import Union
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Key Point: Track the current max node value. Update the answer at every
        node (whether condition is met).

        Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

        Method: Using DFS, traverse the tree. At each node, track the maximum
        node value encountered so far. Iterate answer if "good node" condition
        is met. Call method recursively for left and right subtrees. Return
        accumulated answer.

        Returns: Number of "good" nodes in the binary tree. A node is "good" if
        there are no nodes between it and the root with a greater value. The root
        is always a good node.
        """
        def dfs(node: Optional[TreeNode], current_max: Union[int, float]) -> int:
            if not node:
                return 0
            left = dfs(node.left, max(current_max, node.val))
            right = dfs(node.right, max(current_max, node.val))
            num_good_nodes = left + right
            if current_max <= node.val:
                num_good_nodes += 1
            return num_good_nodes
            
        return dfs(root, float("-inf"))