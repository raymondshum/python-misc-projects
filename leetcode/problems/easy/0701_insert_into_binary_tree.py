class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Key Point: Add node without balancing BST.

        Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/

        Method: Use recursion to traverse to the end of
        the BST. Setting node.left & node.right to the
        value of the recursive call either maintains
        the existing structure or appends the node to a
        leaf.

        Returns: The root node of the BST or a node of 
        passed val if the root is None.
        """
        if not root:
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root