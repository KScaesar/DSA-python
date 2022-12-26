from typing import List


class Solution:
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    # https://labuladong.github.io/algo/3/28/96/

    def maxProfit_greedy(self, prices: List[int]) -> int:
        size = len(prices)
        _min = prices[0]
        ans = 0
        for i in range(1, size):
            _min = min(_min, prices[i])
            ans = max(ans, prices[i] - _min)
        return ans

    def maxProfit_v2(self, prices: List[int]) -> int:
        # monotonic stack
        # 算法筆記 p272

        stack = []  # 定義元素內部為遞減 4 3 2 1
        ans = 0

        # 後進先出的特性 以及 讓大的數值在stack底部
        # 需要倒數進行
        for i in range(len(prices) - 1, -1, -1):
            while len(stack) != 0 and stack[-1] <= prices[i]:
                stack.pop()

            print(stack)
            if len(stack) != 0:
                # 跟頂端元素比的話, 只能得到 下一個更大的值
                # 跟底部元素比, 才能得到後面的最大
                # ans = max(ans, stack[-1] - prices[i])
                ans = max(ans, stack[0] - prices[i])
            stack.append(prices[i])

        return ans

    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)

        # dp[i][k][has] 第 i 天, k 次交易, 持有股票 時, 有多少錢
        # 三種選擇 進行買, 進行賣, 維持
        # 状态 k 的定义并不是「已进行的交易次数」，而是「最大交易次数的上限限制」。
        # 如果确定今天进行一次交易，且要保证截至今天最大交易次数上限为 k，那么昨天的最大交易次数上限必须是 k - 1
        # 在选择 buy 的时候相当于开启了一次交易，那么对于昨天来说，交易次数的上限 k 应该减小 1
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        dp_not = [0] * size  # 沒有股票的狀態
        dp_has = [0] * size  # 擁有股票的狀態

        # base case
        dp_not[0] = 0
        dp_has[0] = -prices[0]

        # for 0 <= i < n:
        #     for 1 <= k <= K:
        #         for s in {0, 1}:
        #             dp[i][k][s] = max(buy, sell, rest)

        for i in range(1, size):
            dp_not[i] = max(dp_has[i - 1] + prices[i], dp_not[i - 1])
            dp_has[i] = max(- prices[i], dp_has[i - 1])

        # print(dp_not)
        # print(dp_has)
        return dp_not[-1]


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit_v2([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit_greedy([7, 1, 5, 3, 6, 4]))
