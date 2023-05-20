class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Key Point: Use the property of Binary Search Trees to
        include or exclude subtrees based on value of the 
        current node.

        Link: https://leetcode.com/problems/range-sum-of-bst/description/

        Method: Consider the property of BSTs. At a given node,
        if the node's value is <= the low watermark, then every
        node in the left subtree will be below the cutoff. If
        value is >= to the high watermark, then every node in
        the right subtree will be above the cutoff.

        Returns: Sum of all node values in an inclusive range or
        0 if the root is None.
        """
        if not root:
            return 0
        
        ans = 0
        
        if low <= root.val <= high:
            ans += root.val
        if root.val > low:
            ans += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            ans += self.rangeSumBST(root.right, low, high)
        
        return ans