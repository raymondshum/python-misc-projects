class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Key Point: Use DFS to track number of directly connected
        nodes (area) within each disjoint set of connected nodes
        (islands) in a 2D matrix, representing a map.

        Link: https://leetcode.com/problems/max-area-of-island/

        Method: Use DFS. Iterate through the grid, checking if
        the element is equal to "1" and has not been previously
        visited. If so, use DFS to recursively explore all
        connected elements, tracking the number of connected
        elements (area). If the current area is larger than the
        max area, then record the current value as the new max.
        Track all visisted elements in a set. Repeat for all
        elements.

        Returns: Int representing the maximum number of directly
        connected elements in a group of connected elements in
        the grid.
        """
        MAX_ROW:    int                   = len(grid)
        MAX_COL:    int                   = len(grid[0])
        DIRECTIONS: List[Tuple[int, int]] = [(1,0), (-1,0), (0,1), (0,-1)]
        visited:    Set(int)              = set()
        max_area:   int                   = 0

        def is_valid(row_num: int, col_num: int) -> bool:
            return 0 <= row_num < MAX_ROW \
                and 0 <= col_num < MAX_COL \
                and grid[row_num][col_num] == 1 \
                and (row_num, col_num) not in visited
        
        def dfs_explore(row_num: int, col_num: int) -> int:
            visited.add((row_num, col_num))
            area: int = 1
            for d_row, d_col in DIRECTIONS:
                next_row_id: int = row_num + d_row
                next_col_id: int = col_num + d_col
                if is_valid(next_row_id, next_col_id):
                    area += dfs_explore(next_row_id, next_col_id)
            return area
        
        for row_id, row in enumerate(grid):
            for col_id, col in enumerate(row):
                if not is_valid(row_id, col_id):
                    continue
                max_area = max(max_area, dfs_explore(row_id, col_id))
        
        return max_area