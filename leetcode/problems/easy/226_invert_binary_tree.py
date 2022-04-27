from leetcode.data_structures.tree_node import TreeNode, bfs_print
from typing import Optional

class Solution:
    def swap_node(self, root, left, right):
        if not root:
            return
        
        temp_node = left
        root.left = right
        root.right = temp_node
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Key Point: Use a temp node to swap left and right nodes.
        
        Link: https://leetcode.com/problems/invert-binary-tree/submissions/
        
        Method: Recursive method. For each node, return if its None. Else, swap the
        left and right nodes. Then call invert on the child nodes.

        Returns:
            Optional[TreeNode]: Head of inverted binary tree.
        """        
        
        # swap using a temp node
        if not root:
            return
        
        self.swap_node(root, root.left, root.right)
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
def main():
    input = {
    0: {
        "root": [1,2,3,4,5]
    },
    1: {
        "root": [1,2]
    },

    }
    output = [
        [2,3,1],
        []
    ]

    # TODO: implement Tree data structure for test driver
if __name__ == '__main__':
    main()