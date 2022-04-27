from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

# From https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
def bfs_print(visited: List[TreeNode], queue: List[TreeNode], graph: List[TreeNode], node: TreeNode):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)