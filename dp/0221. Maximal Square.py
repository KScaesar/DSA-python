import collections
from typing import List


class Solution:
    # https://leetcode.com/problems/maximal-square/
    def maximalSquare_dp(self, matrix: List[List[str]]) -> int:
        # https://leetcode.com/problems/maximal-square/solutions/600149/python-thinking-process-diagrams-dp-approach/?orderBy=most_votes

        # 本題目需要 dp 解法

        m = len(matrix)
        n = len(matrix[0])

        # dp[m][n] 以 matrix[m][n] 為結尾的 最大 方形 邊長是多少?
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        max_side = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    # Be careful of the indexing since dp grid has additional row and column
                    dp[r + 1][c + 1] = min(dp[r][c], dp[r + 1][c], dp[r][c + 1]) + 1
                    max_side = max(max_side, dp[r + 1][c + 1])

        return max_side ** 2

    def maximalSquare_bfs(self, matrix: List[List[str]]) -> int:
        # 得到答案, 但是會 timeout

        # 容易忽略 方形限制
        # 就算想到有方形限制, 條件判斷 一直寫錯
        # 太多要考慮的

        def bfs(matrix, row, col, visited) -> int:
            q = collections.deque([(row, col)])
            ans = 0

            # 錯誤寫法
            # 完全不需要 square_limit
            # level_limit = square_limit - max(row, col)
            level_limit = min(m - row, n - col)

            level = 1
            while q:
                size = len(q)
                # level +=1 # 錯誤的位置, level 更新要放在下方

                for _ in range(size):
                    r, c = q.popleft()
                    if matrix[r][c] == '0':
                        return ans

                    # 容易忽略的條件之1
                    # 而且一直寫錯
                    if r == row + level_limit - 1 or c == col + level_limit - 1:
                        continue

                    for d in dirs:
                        next_r, next_c = r + d[0], c + d[1]
                        _next = (next_r, next_c)
                        if _next in visited:
                            continue

                        if 0 <= next_r < m and 0 <= next_c < n:
                            visited.add(_next)
                            q.append(_next)

                ans = level ** 2  # 表示這層節點, 都通過條件判斷

                # 更新 level 要放這裡
                # https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/bfs-suan-f-463fd/
                level += 1

            return ans

        m = len(matrix)
        n = len(matrix[0])
        square_limit = min(m, n)
        dirs = ((1, 0), (0, 1), (1, 1))

        # tool.print_matrix(matrix)
        result = 0
        for row in range(m):
            for col in range(n):
                sub = bfs(matrix, row, col, set())
                if sub == square_limit ** 2:
                    return sub
                result = max(result, sub)
        return result


if __name__ == '__main__':
    m1 = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    print(Solution().maximalSquare_bfs(m1))
    print(Solution().maximalSquare_dp(m1))
    print()

    m2 = ['0111', '1111', '1111']
    print(Solution().maximalSquare_bfs(m2))
    print(Solution().maximalSquare_dp(m2))
    print()

    m3 = [["1", "1"]]
    print(Solution().maximalSquare_bfs(m3))
    print(Solution().maximalSquare_dp(m3))
    print()

    m4 = [["1", "1", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"]]
    print(Solution().maximalSquare_bfs(m4))
    print(Solution().maximalSquare_dp(m4))
    print()

    m5 = [["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["0", "0", "0", "0", "0"], ["1", "1", "1", "1", "1"],
          ["1", "1", "1", "1", "1"]]
    print(Solution().maximalSquare_bfs(m5))
    print(Solution().maximalSquare_dp(m5))
    print()
