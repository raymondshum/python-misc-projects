class Solution:
    """
    Key Point: Target sum must be 0 at a leaf node for path sum to exist.

    Link: https://leetcode.com/problems/path-sum/description/

    Method: Traverse each path from root to node, subtracting the value
    of the node from the targetSum at each traversal. If the value is 0 at
    the leaf node, then the sum of the path adds exactly to the target sum.

    Returns: True if path sum exists or False otherwise.
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root: Optional[TreeNode], targetSum: int) -> bool:
            if not root:
                return False
            currentSum = targetSum - root.val
            if not root.left and not root.right:
                return currentSum == 0
            return dfs(root.left, currentSum) or dfs(root.right, currentSum)
        return dfs(root, targetSum)