from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        Key Point: Return the sum of the nodes in the lowest level
        of the tree.

        Link: https://leetcode.com/problems/deepest-leaves-sum/description/

        Method: Use BFS. If every node added to the queue does not
        have any children, then you are at the deepest level. Return
        the sum of the nodes. You can calculate it based on the queue
        or keep a running total.

        Returns: An int representing the sum of the nodes at the deepest
        level of the tree or 0 if the root is None.
        """
        if not root:
            return 0
        
        queue = deque([root])

        while queue:
            num_nodes_in_level = len(queue)
            is_lowest_level = True
            level_sum = 0

            for _ in range(num_nodes_in_level):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    is_lowest_level = False
                    queue.append(node.left)
                if node.right:
                    is_lowest_level = False
                    queue.append(node.right)
                
            if is_lowest_level:
                return level_sum
        
        return -1