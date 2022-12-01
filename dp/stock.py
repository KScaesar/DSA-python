# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solutions/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems/
# https://labuladong.github.io/algo/1/13/
#
# 动态规划核心套路 说过
# 动态规划算法本质上就是穷举「状态」，然后在「选择」中选择最优解
#
# 第一步 穷举「状态」，然后在「选择」中选择最优解
# 第二步 有哪些狀態, 第i天 交易k次 是最明顯的狀態
# 第三步 有哪些選擇, sell buy 以及 rest 不做任何事情
# 第四步 列出狀態轉移函數, 發現進行選擇的時候
#       缺乏一個資訊, 讓我們難以進行選擇, 也就是 要手上有股票才能賣, 沒股票才能買
#       這樣一個不容易觀察到的狀態 也就是 目前手上是否有股票 has
# 第五步 把 dp 分為兩個部份進行分析 dp[i][T][0] dp[i][T][1]
# 其 它  只有購買操作會更改允許的最大交易數量
# base  T[-1][k][0] = 0, T[-1][k][1] = -Infinity
#       T[i][0][0] = 0, T[i][0][1] = -Infinity
#
# 此问题共 n × K × 2 种状态，全部穷举就能搞定。
# for 0 <= i < n:
#     for 1 <= k <= K:
#         for s in {0, 1}:
#             dp[i][k][s] = max(buy, sell, rest)

class Solution:

    @staticmethod
    def max_profit_i(prices: list[int]) -> int:
        # leetcode 121
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

        # dp[0][i] 第 i 天 沒股票的最大利潤
        # dp[1][i] 第 i 天 有股票的最大利潤
        n = len(prices)
        dp = [[0 for _ in range(n)] for _ in range(2)]

        # base
        dp[1][0] = float('-inf')  # 第一天 手上有股票 最大利潤為不存在

        for i in range(1, n):
            # 第 i 天 沒股票的最大利潤, 存在兩種情況
            # 1. i-1天 買股票, i 天 賣掉
            # 2. i-1天 沒股票, i 天 沒任何動作
            dp[0][i] = max(dp[1][i - 1] + prices[i], dp[0][i - 1])

            # 第 i 天 有股票的最大利潤, 存在兩種情況
            # 與上述同理
            #
            # 因為只交易一次, 所以不需要 dp[0][i - 1]
            # dp[1][i] = max(dp[0][i - 1] - prices[i], dp[1][i - 1])
            dp[1][i] = max(-prices[i], dp[1][i - 1])

        print(dp)
        return dp[0][n - 1]

    def max_profit_iv(self, k: int, prices: list[int]) -> int:
        # leetcode 188
        # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
        pass


if __name__ == '__main__':
    obj = Solution()

    sol1 = obj.max_profit_i([7, 1, 5, 3, 6, 4])
    print(f'max_profit_i = {sol1}')
