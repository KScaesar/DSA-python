from typing import List


class Solution:
    # https://leetcode.com/problems/minimum-cost-for-tickets/

    # https://leetcode.com/problems/minimum-cost-for-tickets/solutions/226659/Two-DP-solutions-with-pictures/

    # dp 問題

    def mincostTickets_v1(self, days: List[int], costs: List[int]) -> int:

        c1, c7, c30 = costs

        # dp[i] 表示游玩到第 i 天时所需要的最小花费
        dp = [-1] * (days[-1] + 1)

        # base case
        dp[0] = 0  # 第 0 天, 沒辦法玩

        i = 0
        for d in range(1, days[-1] + 1):
            if d == days[i]:
                # 利用 max 避免 index 越界
                dp[d] = min(
                    dp[d - 1] + c1,
                    dp[d - min(d, 7)] + c7,
                    dp[max(0, d - 30)] + c30,
                )
                i += 1
            else:
                dp[d] = dp[d - 1]  # 沒有遊玩的日子, 之前花的錢, 保持原樣

        # print(dp)
        return dp[days[-1]]

    def mincostTickets_dfs(self, days: List[int], costs: List[int]) -> int:
        # timeout

        # 想嘗試用 backtrack
        # 卻一直失敗
        # 感覺花費的錢 和 遊玩的天數, 一直差距一天
        # 要好好參考 combine 寫法, 才能了解, 為什麼差一天

        # 可參考
        # 0139. Word Break

        # dfs 的定義方式, 可以參考 combine 寫法
        # 1. cursor n, track 為 n 的結果
        # 2, cursor n, track 為 n-1 的結果
        #
        # 第二個寫法會比較程式簡潔, 起點不需要有 for 迴圈

        def dfs(days, cost_pair, cursor, cost, track):
            nonlocal ans
            if cursor >= len(days):
                if ans > cost:
                    ans = cost
                    print(cost, track)
                return

            for i in range(len(cost_pair)):
                day, c = cost_pair[i]
                k = cursor
                start_day = days[cursor]

                while k < len(days) and (days[k] - start_day + 1) <= day:
                    k += 1

                # cursor n, track 為 n-1 的結果
                # track.append 的時候, 是用 cursor
                track.append((cursor, c))
                dfs(days, cost_pair, k, cost + c, track)
                track.pop()

        ans = float('inf')
        costs_pair = [(1, costs[0]), (7, costs[1]), (30, costs[2])]

        cost = 0
        # cursor n, track 為 n-1 的結果
        # cursor n, 到達 n-1 所花的錢
        dfs(days, costs_pair, 0, cost, [])
        return ans


if __name__ == '__main__':
    print(Solution().mincostTickets_v1([1, 4, 6, 7, 8, 20], [2, 7, 15]))
    print(Solution().mincostTickets_dfs([1, 4, 6, 7, 8, 20], [2, 7, 15]))
