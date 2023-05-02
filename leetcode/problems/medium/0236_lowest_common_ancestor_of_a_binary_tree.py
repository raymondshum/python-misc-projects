class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Key Point: Three cases: (1) Root is LCA, (2) LCA is on left subtree, (3) LCA is on
        right subtree.

        Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

        Method: Use DFS to split the tree into subtrees. Check for each of the three cases in
        each subtree. Note that a node can be its own descendent. Therefore, if a node matches
        either p or q descendents, then it is also the LCA. If one descendent is found in 
        the left and right subtrees, each, then the root is the LCA (since it links the two
        subtrees).

        Returns: The LCA if it exists or None if it does not.
        """
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left or right