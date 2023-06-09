from collections import deque
class Solution:
    """
    Key Point: Use BFS. Add all 0's to queue first. Then
    track level order for 1's encountered at each step.

    Link: https://leetcode.com/problems/01-matrix/

    Method: Use BFS. Add all zeroes to the queue (do not
    start with 1's for efficiency). Track seen nodes with
    a set. Visit unvisited nodes in each direction, 
    tracking num steps (per level). Num steps to reach
    the cell is returned as a 2d matrix as the result.

    Returns: 2D list of ints representing num steps
    distance from the nearest 0.
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        MAX_ROWS:   int                        = len(mat)
        MAX_COLS:   int                        = len(mat[0])
        DIRECTIONS: List[int, Tuple[int, int]] = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        result: List[List[int]] = [[0 for _ in range(MAX_COLS)] for _ in range(MAX_ROWS)]
        visited: Set[Tuple[int, int]] = set()
        queue: Deque[Tuple[int, int, int]] = deque()

        def is_valid(row_num: int, col_num: int):
            return 0 <= row_num < MAX_ROWS \
                and 0 <= col_num < MAX_COLS \
                and (row_num, col_num) not in visited

        # Add all 0's to queue
        for row_num, row in enumerate(mat):
            for col_num, col in enumerate(mat[row_num]):
                if mat[row_num][col_num] == 1:
                    continue
                queue.append(((row_num, col_num, 0)))
                visited.add((row_num, col_num))
        
        while queue:
            row_num, col_num, num_steps = queue.popleft()
            for row_mod, col_mod in DIRECTIONS:
                next_row_num:  int = row_num + row_mod
                next_col_num:  int = col_num + col_mod
                next_step_num: int = num_steps + 1
                if not is_valid(next_row_num, next_col_num):
                    continue
                visited.add((next_row_num, next_col_num))
                queue.append((next_row_num, next_col_num, next_step_num))
                result[next_row_num][next_col_num] = next_step_num

        return result