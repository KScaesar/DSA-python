import random
from tool import debugHelper


def knapsack_01_backtrace(wt: list[int], val: list[int], W: int) -> int:
    # count: int = 0
    # space = '  '

    # @debugHelper
    def backtrace1(wt: list[int], val: list[int], W: int, total: int) -> int:
        # nonlocal count
        # nonlocal space

        # 由於下方選擇 coin 的時候
        # total+v 的 total 數值必須固定不變
        # 而 result 隨著每次選擇, 會不斷變化數值
        # 所以必須分成兩個變數 result, total
        result = total
        # print(f'{space*count}enter wt={wt},W={W},result={result}')

        if len(wt) == 0:
            # print(f'{space*count}return wt={wt},W={W},result={result}')
            return result

        for i, _ in enumerate(wt):
            w = wt.pop(i)
            v = val.pop(i)

            if W-w > 0:
                # count = count+1
                result = max(result, backtrace1(wt, val, W-w, total+v))
                # count = count-1

            wt.insert(i, w)
            val.insert(i, v)

        # print(f'{space*count}return wt={wt},W={W},result={result}')
        return result

    # 本題 backtrace1 backtrace2
    # 可以和 balloon_leetcode312 互相參考
    # 為什麼寫法略有不同

    result = float('-inf')

    def backtrace2(wt: list[int], val: list[int], W: int, total: int):
        nonlocal result
        result = max(result, total)

        if len(wt) == 0:
            return

        for i, _ in enumerate(wt):
            w = wt.pop(i)
            v = val.pop(i)

            if W-w > 0:
                backtrace2(wt, val, W-w, total+v)

            wt.insert(i, w)
            val.insert(i, v)

        return

    backtrace2(wt, val, W, 0)
    return result


def can_partition_backtrace(nums: list[int]) -> bool:
    N = len(nums)
    W = sum(nums)//2

    # @debugHelper
    def backtrace1(N: int, W: int, pick: list[int]) -> bool:
        nonlocal nums

        if N >= 0 and W == 0:
            return True
        elif N == 0 and W != 0:
            return False

        for i in range(N):
            if nums[i] > W:
                continue

            w = nums.pop(i)
            pick.append(w)
            result = backtrace1(N-1, W-w, pick)
            nums.insert(i, w)

            if result:
                return True
            else:
                pick.pop()

        return False

    # @debugHelper
    def backtrace2(index_record: dict[int, bool], W: int, pick: list[int]) -> bool:
        nonlocal nums
        N = len(nums)

        if N >= 0 and W == 0:
            return True
        elif N == 0 and W != 0:
            return False

        for i in range(N):
            w = nums[i]
            if index_record.get(i, False) or w > W:
                continue

            pick.append(w)
            index_record[i] = True
            subproblem = backtrace2(index_record, W-w, pick)
            index_record[i] = False

            if subproblem:
                return True
            else:
                pick.pop()

        return False

    # return backtrace1(N, W, [])
    return backtrace2(dict(), W, [])


def can_partition_dp(nums: list[int]) -> bool:
    # 算法筆記 p198

    N = len(nums)
    W = sum(nums)//2

    dp = [[False]*(W+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = True

    # print(dp)

    for i in range(1, N+1):
        for w in range(1, W+1):
            if nums[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # 算法筆記 p196, p200
                # 反覆著墨 裝入的情況
                # 想清楚每項 i-1 代表什麼意思
                dp[i][w] = dp[i-1][w] or dp[i-1][w-nums[i-1]]

    # print(dp)
    return dp[N][W]


def coin_change_dp_v1(amount: int, coins: list[int]) -> int:
    # 算法筆記 p202

    N = len(coins)
    dp = [[0]*(amount+1) for _ in range(N+1)]
    for i in range(N+1):  # 不要忘記, row 數量為 N+1
        dp[i][0] = 1

    # 記得從1開始
    for i in range(1, N+1):
        for j in range(1, amount+1):
            # print(i, j)
            if j < coins[i-1]:  # coin arry 和 dp array, 其 index 差距1
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-coins[i-1]]

    return dp[N][amount]


def coin_change_dp_v2(amount: int, coins: list[int]) -> int:
    # 算法筆記 p205 空間優化版本

    N = len(coins)
    dp = [0]*(amount+1)
    dp[0] = 1

    for i in range(N):
        for j in range(1, amount+1):
            if j >= coins[i]:
                dp[j] += dp[j-coins[i]]

    return dp[amount]


if __name__ == '__main__':
    sol1 = knapsack_01_backtrace([2, 1, 3], [4, 2, 3], 4)
    print(f'{knapsack_01_backtrace.__name__} = {sol1}\n')

    ##

    # can_partition_input = [1, 6, 4, 9]
    # can_partition_input = [1, 5, 11, 5]
    can_partition_input = [1, 3, 2, 8]

    sol2 = can_partition_backtrace(can_partition_input)
    print(f'{can_partition_backtrace.__name__} = {sol2}\n')

    sol3 = can_partition_dp(can_partition_input)
    print(f'{can_partition_dp.__name__} = {sol3}\n')

    ##

    coin_change_input = (5, [1, 2, 5])

    sol4 = coin_change_dp_v1(*coin_change_input)
    print(f'{coin_change_dp_v1.__name__} = {sol4}\n')

    sol5 = coin_change_dp_v2(*coin_change_input)
    print(f'{coin_change_dp_v2.__name__} = {sol5}\n')
