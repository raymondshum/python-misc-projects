class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Key Point: Use the property of inorder traversal to
        build a sorted list.

        Link: https://leetcode.com/problems/closest-binary-search-tree-value/

        Method: Build an sorted list through inorder DFS 
        traversal. Then calculate the distance between the 
        target and current value per element of the list,
        returning the element with the smallest distance.

        Returns: The node value closest to the target number.
        """
        def build_inorder_list(node: TreeNode) -> List[int]:
            if not node:
                return []
            left = build_inorder_list(node.left)
            right = build_inorder_list(node.right)
            return left + [node.val] + right
        return min(build_inorder_list(root), key = lambda x: abs(target-x))