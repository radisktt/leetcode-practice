from typing import List


from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_dict = {}
        ans = 0

        # Count occurrences of rows in the grid
        for i in range(len(grid)):
            row_tuple = tuple(grid[i])
            if row_tuple not in grid_dict:
                grid_dict[row_tuple] = 1
            else:
                grid_dict[row_tuple] += 1

        # Check for equal pairs using columns
        for i in range(len(grid)):
            col_tuple = tuple(grid[j][i] for j in range(len(grid)))
            if col_tuple in grid_dict:
                ans += grid_dict[col_tuple]

        return ans
