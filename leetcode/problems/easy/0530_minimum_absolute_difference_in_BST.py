class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Key Point: Note that inorder traversal using DFS on
        a BST will allow you to perform operations on each
        node in sorted, ascending order.

        Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

        Method: Use inorder DFS traversal to get a sorted
        list of node values and then find the minimum between
        two values.

        Returns: An int representing the minimum difference
        between the values of two nodes or -1 if the root is
        None.
        """
        def dfs(node: Optional[TreeNode], sorted_nodes: List[int]) -> List[int]:
            if not node:
                return
            
            dfs(node.left, sorted_nodes)
            sorted_nodes.append(node.val)
            dfs(node.right, sorted_nodes)
        
        if not root:
            return -1

        sorted_nodes = []
        dfs(root, sorted_nodes)
        
        current_min = float(inf)
        for index in range(1, len(sorted_nodes)):
            current_min = min(current_min, sorted_nodes[index] - sorted_nodes[index - 1])
        return current_min
