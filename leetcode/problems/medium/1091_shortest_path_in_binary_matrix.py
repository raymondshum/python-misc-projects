from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Key Point: Use BFS to determine the shortest path.

        Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/

        Method: Use BFS. Track number of steps as you add each connected
        node to the queue (each level has the same step). Track visited
        nodes in a set to prevent backtracking. Return the number of steps
        as soon as the bottom left node is reached.

        Returns: Int representing the length of the shortest path from
        the top left cell to the bottom right cell of the input grid.
        """
        PATH_BLOCKED:   int = 1
        PATH_OPEN:      int = 0
        NO_PATH_EXISTS: int = -1
        MAX_ROW_NUM:    int = len(grid) - 1
        MAX_COL_NUM:    int = len(grid[0]) - 1
        DESTINATION:    int = (MAX_ROW_NUM, MAX_COL_NUM)

        if grid[0][0] == PATH_BLOCKED:
            return NO_PATH_EXISTS

        visited:    Set[Tuple[int, int]]              = set((0,0))
        queue:      Deque[List[Tuple[int, int, int]]] = deque([(0,0,1)])
        directions: List[Tuple[int, int]]             = [
                                                            (1, -1), (1, 0), (1, 1),
                                                            (0, -1), (0, 1),
                                                            (-1, 1), (-1, 0), (-1, -1)
                                                        ]

        def is_valid(row_num: int, col_num: int):
            return 0 <= row_num <= MAX_ROW_NUM \
                and 0 <= col_num <= MAX_COL_NUM \
                and grid[row_num][col_num] == PATH_OPEN \
                and (row_num, col_num) not in visited

        while queue:
            row_num, col_num, num_steps = queue.popleft()

            if (row_num, col_num) == DESTINATION:
                return num_steps

            for row_mod, col_mod in directions:
                next_row_num = row_num + row_mod
                next_col_num = col_num + col_mod
                if not is_valid(next_row_num, next_col_num):
                    continue
                # Track visited here because only the first to arrive matters.
                visited.add((next_row_num, next_col_num))
                queue.append((next_row_num, next_col_num, num_steps + 1))

        return NO_PATH_EXISTS