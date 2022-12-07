import collections

from graph.union_find import UnionFind


class Solution:
    # https://leetcode.com/problems/number-of-islands/

    # 方法1: dfs, bfs
    # 方法2: union-find
    def numIslands_union_find(self, grid: list[list[str]]) -> int:
        # https://haogroot.com/2021/01/29/union_find-leetcode/

        rows = len(grid)
        cols = len(grid[0])
        uf = UnionFind([x for x in range(rows * cols)])

        directions = self.directions()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0':
                    uf.component_count -= 1
                    continue

                direction = []

                # matrix 順序尋訪, 分成四大區塊
                # A. 左上方 最大範圍
                # B. 右方 狹長範圍
                # C. 下方 狹長範圍
                # D. 右下方 最小範圍
                if rows - 1 > row >= 0 and cols - 1 > col >= 0:
                    # A
                    direction = [directions["right"], directions["down"]]
                elif rows - 1 > row >= 0 and col == cols - 1:
                    # B
                    direction = [directions["left"], directions["down"]]
                elif row == rows - 1 and cols - 1 > col >= 0:
                    # C
                    direction = [directions["right"]]
                elif row == rows - 1 and col == cols - 1:
                    # D
                    pass

                for d in direction:
                    next_row = row + d["y"]
                    next_col = col + d["x"]
                    # print(f' now={[row, col]} next={[next_row, next_col]} d={d}')
                    if grid[next_row][next_col] == '0':
                        continue
                    uf.union_v1(row * cols + col, next_row * cols + next_col)

        return uf.component_count

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.count = 0

    def directions(self) -> dict[str, dict[str, int]]:
        return {
            "right": {"x": 1, "y": 0},
            "left": {"x": -1, "y": 0},
            "up": {"x": 0, "y": -1},
            "down": {"x": 0, "y": 1},

            # 用 for loop 尋訪陣列
            # 注意上下的定義
            # "up": {"x": 0, "y": 1},
            # "down": {"x": 0, "y": -1},
        }

    def numIslands_dfs(self, grid: list[list[str]]) -> int:
        # https://labuladong.github.io/algo/4/31/107/

        # dfs 如何用 stack 達成
        # https://youtu.be/bD8RT0ub--0?list=PLAnjpYDY-l8IacYv_2lIZxNrQmkY3paSN&t=660

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.count = 0

        def dfs(grid, m, n):
            if m < 0 or n < 0 or m >= self.rows or n >= self.cols:
                return

            # 利用原本的陣列, 充當 seen
            # 此條件同時也可以判斷 該節點是否為終點
            if grid[m][n] == '0' or grid[m][n] == '-1':
                return
            grid[m][n] = '-1'  # -1 表示已經尋訪過
            # self.print_grid(grid)

            for d in list(self.directions().values()):
                next_m = m + d['y']
                next_n = n + d['x']
                dfs(grid, next_m, next_n)

        # 因為 dfs 是找出 兩個節點之間的所有路徑
        # 所以需要用 for loop 對 所有節點進行尋訪
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == '1':
                    self.count += 1  # 重點: 在一個很巧妙的位置 進行+1
                    dfs(grid, i, j)
                    # self.print_grid(grid)

        return self.count

    def numIslands_bfs(self, grid: list[list[str]]) -> int:

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.count = 0

        q = collections.deque([])  # 要記得給一個空陣列初始化 deque

        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == '0' or grid[i][j] == '-1':
                    continue
                elif grid[i][j] == '1':
                    q.append((i, j))
                    grid[i][j] = '-1'  # -1 is seen signal
                    self.count += 1
                    # self.print_grid(grid)

                while len(q) != 0:
                    size = len(q)
                    for _ in range(size):
                        row, col = q.popleft()
                        for d in list(self.directions().values()):
                            next_row = row + d['y']
                            next_col = col + d['x']

                            if next_row < 0 or next_row == self.rows or next_col < 0 or next_col == self.cols:
                                continue

                            # print(f' now={[row, col]} next={[next_row, next_col]} d={d}')
                            if grid[next_row][next_col] == '1':
                                q.append((next_row, next_col))
                                grid[next_row][next_col] = '-1'
                                # self.print_grid(grid)

                # self.print_grid(grid)

        return self.count

    def print_grid(self, grid: list[list[str]]):
        self.rows = len(grid)
        self.cols = len(grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                print(f' {grid[i][j]:{2}} ', end='')
            print()
        print()


if __name__ == '__main__':
    obj = Solution()
    # grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(f'union-find = {obj.numIslands_union_find(grid)}')

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["1", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(f'dfs = {obj.numIslands_dfs(grid)}')

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["1", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(f'bfs = {obj.numIslands_bfs(grid)}')
