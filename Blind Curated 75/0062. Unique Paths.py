class Solution:
    # https://leetcode.com/problems/unique-paths/

    # dp
    def uniquePaths_v2(self, m: int, n: int) -> int:
        # 空間壓縮版本
        # 不熟悉 要再多看幾次

        # 解釋空間優化的演進
        # https://leetcode.com/problems/unique-paths/solutions/22954/c-dp/?orderBy=most_votes

        # 只能降為 1D
        # 無法降為 常數

        dp = [0] * n

        # 投影後, 應該把 1D 都給初始值
        # dp[0] = 1
        # dp[1] = 1
        #
        # base case
        for k in range(n):
            dp[k] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[col] = dp[col] + dp[col - 1]  # dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1]

    def uniquePaths(self, m: int, n: int) -> int:
        # dp[y][x] 走到 (x,y) 有幾種方法
        dp = [[0] * n for _ in range(m)]

        # 要詢問走到原點不動, 是否需要算一種路徑
        dp[0][0] = 1

        # base case
        for row in range(1, m):
            dp[row][0] = 1
        for col in range(1, n):
            dp[0][col] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
    print(Solution().uniquePaths_v2(3, 7))
