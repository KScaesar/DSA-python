from typing import List


class Solution:
    # https://leetcode.com/problems/number-of-islands/
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(grid, col, row, n, m):
            print(f'row={row} col={col}')

            if grid[row][col] == '0' or grid[row][col] == '-1':
                return
            # view(grid)

            grid[row][col] = '-1'  # visited
            for d in direction:
                x, y = d
                if 0 <= row + y < m and 0 <= col + x < n:
                    dfs(grid, col + x, row + y, n, m)

        for i in range(m * n):
            row = i // n
            col = i % n
            print(f'row={row} col={col} m={m} n={n}')
            if grid[row][col] == '1':
                count += 1
                dfs(grid, col, row, n, m)

        return count


def view(grid):
    m = len(grid)
    n = len(grid[0])
    for row in range(m):
        for col in range(n):
            print(f'{grid[row][col]:>2}', end='')
        print()
    print()


if __name__ == '__main__':
    # print(
    #     Solution().numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))

    # print(
    #     Solution().numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))

    print(
        Solution().numIslands([["1", "0", "1", "1", "0", "1", "1"]]))
