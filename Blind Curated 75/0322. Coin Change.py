import collections
from typing import List

import tool


class Solution:
    # https://leetcode.com/problems/coin-change/

    # 也有 bfs 的解法
    # 尋找最少硬幣的解決方案（比如從 0 到 amount 的最短路徑）
    # 比 dp 更快
    # https://leetcode.com/problems/coin-change/solutions/77361/fast-python-bfs-solution/?orderBy=most_votes

    def coinChange_bfs(self, coins: List[int], amount: int) -> int:
        queue = collections.deque([amount])
        level = -1

        # 如果沒加上 visited 會出現 timeout 的情況
        visited = [False] * (amount + 1)

        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                node = queue.popleft()

                # 避免走 過去的路
                if visited[node]:
                    continue
                visited[node] = True

                if node == 0:
                    return level

                for v in coins:
                    if node - v >= 0:
                        queue.append(node - v)

        return -1

    def coinChange_dp(self, coins: List[int], amount: int) -> int:
        # https://labuladong.github.io/algo/di-er-zhan-a01c6/dong-tai-g-a223e/dong-tai-g-1e688/
        # 算法筆記 p38

        # 把背包的定義 背下來
        # dp[i][w] 的定义如下：对于前 i 个物品，当前背包的容量为 w，这种情况下可以装的最小組合長度是 dp[i][w]
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]

        # base case
        for i in range(len(coins) + 1):
            dp[i][0] = 0  # 重量為 0, 所有 case 一定是 0

        # 注意 2d陣列 設置 base case, 不要互相覆蓋
        # 應該從 1 開始
        # for w in range( amount + 1):
        for w in range(1, amount + 1):
            # 算法筆記 p43
            # 考虑到递推公式的特性, 會使用到 min
            # 所以應該給 初始值 無限大, 有利於後續取最小值
            dp[0][w] = float("inf")

        tool.print_matrix(dp)

        # 求组合数 就是外层for循环遍历物品，内层for遍历背包
        # 求排列数 就是外层for遍历背包，内层for循环遍历物品
        # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0518.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2II.md
        # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0322.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2.md
        for i in range(1, len(coins) + 1):
            for w in range(1, amount + 1):
                if w >= coins[i - 1]:
                    dp[i][w] = min(
                        dp[i - 1][w],  # 不選擇該硬幣
                        dp[i][w - coins[i - 1]] + 1  # 選擇該硬幣
                    )
                else:
                    # 只能选择不装入背包
                    dp[i][w] = dp[i - 1][w]

        tool.print_matrix(dp)
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

    def coinChange_backtrack(self, coins: List[int], amount: int) -> int:
        # 算法筆記 p28

        def backtrack(coins, start, length, target):
            nonlocal ans
            if target == 0:
                if ans == -1:
                    ans = length
                else:
                    ans = min(ans, length)
                return
            elif target < 0:
                return

            # k 硬幣數量
            # N 目標金額
            #
            # 子問題數量 = k^N
            # 每個子問題 有一個 for 迴圈, 也就是 一個子問題的複雜度是 O(k)
            #
            # 複雜度 子問題數量 * 一個子問題的複雜度
            # O(k
            for i in range(start, len(coins)):
                v = coins[i]
                backtrack(coins, i, length + 1, target - v)

        ans = -1
        backtrack(coins, 0, 0, amount)
        return ans


if __name__ == '__main__':
    print(Solution().coinChange_backtrack([1, 2, 5], 11))
    print(Solution().coinChange_dp([1, 2, 5], 11))
    print(Solution().coinChange_bfs([1, 2, 5], 11))
