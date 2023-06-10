from collections import deque, namedtuple
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        Key Point: Use BFS. Track "state" in the "seen"
        set along with steps. Allow for the case that
        there is no solution.

        Link: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

        Method: Use BFS. At each cell, explore the 4
        cardinal directions. If it's valid, add the
        next move to the queue. Track state in the
        "seen" set. (Meaning track the number of times
        you can destroy an obstacle). This is because
        different paths can approach different obstacles
        with a different history of usage for removal.
        Return num steps once the lower right hand cell
        is reached.

        Returns: Int representing num steps in the 
        shortest path or -1 if none exist.
        """
        CellState = namedtuple(
            "CellState",
            ["row_num", "col_num", "remove_remaining"]
        )
        PathState = namedtuple(
            "PathState",
            ["row_num", "col_num", "num_steps", "remove_remaining"]
        )
        Direction = namedtuple(
            "Direction",
            ["row_mod", "col_mod"]
        )
        MAX_ROW:    int              = len(grid)
        MAX_COL:    int              = len(grid[0])
        DIRECTIONS: List[Direction]  = [(1,0),(-1,0),(0,1),(0,-1)]
        
        seen:       Set[CellState]   = {(0,0,0)}
        queue:      Deque[PathState] = deque([(0,0,0,k)])

        def is_valid(row_num, col_num):
            return 0 <= row_num < MAX_ROW \
                and 0 <= col_num < MAX_COL 

        def bfs_explore(row_num, col_num):
            num_steps: int = 0
            finished: bool = False
            while queue:
                row_num, col_num, num_steps, remove_remaining = queue.popleft()
                if (row_num, col_num) == (MAX_ROW-1, MAX_COL-1):
                    finished = True
                    break
                for row_mod, col_mod in DIRECTIONS:
                    next_row_num: int = row_num + row_mod
                    next_col_num: int = col_num + col_mod
    
                    if not is_valid(next_row_num, next_col_num):
                        continue

                    next_remove_remaining: int = remove_remaining
                    if grid[next_row_num][next_col_num] == 1:
                        if next_remove_remaining == 0:
                            continue
                        next_remove_remaining -= 1

                    if (next_row_num,next_col_num,next_remove_remaining) in seen:
                        continue
                        
                    seen.add((next_row_num, next_col_num, next_remove_remaining))
                    queue.append((next_row_num, next_col_num, num_steps+1, next_remove_remaining))
            return num_steps if finished else -1
        
        return bfs_explore(0,0)
        