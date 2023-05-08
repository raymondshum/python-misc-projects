from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Key Point: Return the rightmost node at each level of the
        binary tree.

        Link: https://leetcode.com/problems/binary-tree-right-side-view/description/

        Method: Use BFS to traverse the tree. Hold the nodes of each
        level in a list. Append the value of the rightmost node to the
        list of answers.

        Returns: The values of the rightmost nodes in the tree or an
        empty list if the root is None.
        """
        if not root:
            return []
        
        queue = deque([root])
        right_side_nodes = []

        while queue:
            
            num_nodes_in_level = len(queue)
            right_side_nodes.append(queue[-1].val)

            for _ in range(num_nodes_in_level):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        
        return right_side_nodes