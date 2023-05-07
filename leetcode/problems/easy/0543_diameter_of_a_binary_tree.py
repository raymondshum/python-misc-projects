class Solution:
    """
    Key point: Add the longest path on the left side
    with the longest path on the right side to find
    the total longest path.

    Link: https://leetcode.com/problems/diameter-of-binary-tree/description/

    Method: Use DFS to traverse the tree recursively. 
    Imagine you start at the leaf. Each leaf is a length
    of 1. The parent above the leaf is a length of 2
    (child node + 1). Taking the max of this & bubbling
    up to root will return the longest unbroken path on
    a given side. Adding paths from both sides will then
    give the longest path between 2 nodes.

    Returns: int representing the longest distance between
    2 nodes or 0 if the root is None.
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def helper(self, node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left = helper(self, node.left)
            right = helper(self, node.right)

            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1
        
        if not root:
            return 0
        
        helper(self, root)
        
        return self.diameter