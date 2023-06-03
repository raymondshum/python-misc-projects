class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Key Point: Explore the graph recursively, moving to
        adjacent cells if they: (1) have not been visited 
        (2) have a value of "1".

        Link: https://leetcode.com/problems/number-of-islands/

        Method: At each cell, check if the cell has been visited
        and if the value is "1". If so, explore adjacent cells
        recursively using the same methodology, marking encountered
        cells as visited. If not, skip to the next cell.

        Returns: Int representing the number of disconnected clusters
        of 1's in the grid (islands).
        """
        steps: List[Tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row_len: int = len(grid)
        col_len: int = len(grid[0])
        seen: Set[Tuple[int, int]] = set()
        num_islands: int = 0

        def is_valid(row_num: int, col_num: int) -> bool:
            return 0 <= row_num < row_len \
                and 0 <= col_num < col_len \
                and grid[row_num][col_num] == "1" \
                and (row_num, col_num) not in seen
        
        def dfs_explore(row_num: int, col_num: int) -> None:
            seen.add((row_num, col_num))
            for step_row, step_col in steps:
                next_row_num: int = step_row + row_num
                next_col_num: int = step_col + col_num
                if (not is_valid(next_row_num, next_col_num)):
                    continue
                dfs_explore(next_row_num, next_col_num)
        
        for row_num, _ in enumerate(grid):
            for col_num, _ in enumerate(grid[row_num]):
                if (not is_valid(row_num, col_num)):
                    continue
                num_islands += 1
                dfs_explore(row_num, col_num)
        
        return num_islands