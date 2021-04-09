from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        def dfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = 0
                if i+1 < len(grid) and grid[i+1][j] == "1":
                    dfs(i+1, j)
                if j+1 < len(grid[0]) and grid[i][j+1] == "1":
                    dfs(i, j+1)
                if i-1 >= 0 and grid[i-1][j] == "1":
                    dfs(i-1, j)
                if j-1 >= 0 and grid[i][j-1] == "1":
                    dfs(i, j-1)
            else:
                return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        return cnt


muySolution = Solution()
muySolution.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
])
