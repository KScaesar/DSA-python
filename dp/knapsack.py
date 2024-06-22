from typing import List, Tuple


# https://oi-wiki.org/dp/knapsack/
# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.md

# 矩阵的格式为 m×n
# m is rows
# n is cols
#
# rows = m = 2
# cols = n = 3
# matrix1 = [[0 for _ in range(cols)] for _ in range(rows)]
# matrix2 = [[0] * n for _ in range(m)]
#
# matrix1[rows - 1][cols - 1] = 1
# print(matrix1)
# [[0, 0, 0], [0, 0, 1]]

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-1.md
    # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-2.md

    """
    :param weights: List[int] - 物品的重量
    :param values: List[int] - 物品的價值
    :param capacity: int - 背包的最大容量
    :return: int - 能夠獲得的最大價值

    問題描述：
    給定一個容量為 capacity 的背包和 n 個物品，每個物品有重量 weights[i] 和價值 values[i]。
    求能放入背包的物品的最大總價值。

    解法：
    使用動態規劃。定義 dp[i][w] 為考慮前 i 個物品，在背包容量為 w 時能達到的最大價值。
    狀態轉移方程為：
    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])，其中 1 <= i <= n，1 <= w <= capacity。
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if w >= weights[i - 1]:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1],
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def example_knapsack_01():
    weights = [1, 2, 3]
    values = [6, 10, 12]
    capacity = 5
    max_value = knapsack_01(weights, values, capacity)
    print(f"01 背包問題: 最大價值為 {max_value} (預期輸出: 22)")


def knapsack_complete(weights: List[int], values: List[int], capacity: int) -> int:
    # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80%E5%AE%8C%E5%85%A8%E8%83%8C%E5%8C%85.md

    """
    :param weights: List[int] - 物品的重量
    :param values: List[int] - 物品的價值
    :param capacity: int - 背包的最大容量
    :return: int - 能夠獲得的最大價值

    問題描述：
    給定一個容量為 capacity 的背包和 n 個物品，每個物品有重量 weights[i] 和價值 values[i]。
    每個物品可以選擇多次放入背包，求能放入背包的物品的最大總價值。

    解法：
    使用動態規劃。定義 dp[w] 為背包容量為 w 時能達到的最大價值。
    狀態轉移方程為：
    dp[i][w] = max(dp[i-1][w], dp[i][w - weights[i]] + k * values[i])

    dp[w] = max(dp[w], dp[w - weights[i]] + values[i])，其中 0 <= i < n，weights[i] <= w <= capacity。
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if w >= weights[i - 1]:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i][w - weights[i - 1]] + values[i - 1],
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def example_knapsack_complete():
    weights = [1, 2, 3, 4, 5]
    values = [10, 20, 30, 40, 50]
    capacity = 8
    max_value = knapsack_complete(weights, values, capacity)
    print(f"完全背包問題: 最大價值為 {max_value} (預期輸出: 80)")


def knapsack_multiple(weights: List[int], values: List[int], quantities: List[int], capacity: int) -> int:
    # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80%E5%A4%9A%E9%87%8D%E8%83%8C%E5%8C%85.md

    """
    :param weights: List[int] - 物品的重量
    :param values: List[int] - 物品的價值
    :param quantities: List[int] - 每個物品的數量限制
    :param capacity: int - 背包的最大容量
    :return: int - 能夠獲得的最大價值

    問題描述：
    給定一個容量為 capacity 的背包和 n 個物品，每個物品有重量 weights[i] 和價值 values[i]，以及數量限制 quantities[i]。
    每個物品最多可以選擇 quantities[i] 次放入背包，求能放入背包的物品的最大總價值。

    解法：
    把相同的物品, 拆分成多個物品, 每個物品只能選擇一次, 這樣就可以轉化為 0-1 背包問題。

    一个一个拆：枚举2^511次来表示0-511的所有状态
    二进制拆法：枚举2^9次，但这并不会妨碍他能表示出0-511所有状态
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            for k in range(1, quantities[i - 1] + 1):
                if w >= k * weights[i - 1]:
                    dp[i][w] = max(
                        dp[i - 1][w],
                        dp[i - 1][w - k * weights[i - 1]] + k * values[i - 1],
                    )
                else:
                    dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def example_knapsack_multiple():
    weights = [1, 2]
    values = [1, 2]
    quantities = [2, 1]
    capacity = 5
    max_value = knapsack_multiple(weights, values, quantities, capacity)
    print(f"多重背包問題: 最大價值為 {max_value} (預期輸出: 4)")


def knapsack_fractional(weights: List[int], values: List[int], capacity: int) -> float:
    """
    :param weights: List[int] - 物品的重量
    :param values: List[int] - 物品的價值
    :param capacity: int - 背包的最大容量
    :return: float - 能夠獲得的最大價值

    問題描述：
    給定一個容量為 capacity 的背包和 n 個物品，每個物品有重量 weights[i] 和價值 values[i]。
    物品可以被分割成任意大小，求能放入背包的物品的最大總價值。

    解法：
    使用貪心算法。計算每個物品的價值密度，按照價值密度從大到小選擇物品放入背包，直到背包滿為止。
    """
    n = len(weights)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0
    current_weight = 0

    return total_value


def example_knapsack_fractional():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value = knapsack_fractional(weights, values, capacity)
    print(f"分數背包問題: 最大價值為 {max_value} (預期輸出: ?)")


def knapsack_2d(weights: List[int], values: List[int], volumes: List[int], max_weight: int, max_volume: int) -> int:
    """
    :param weights: List[int] - 物品的重量
    :param values: List[int] - 物品的價值
    :param volumes: List[int] - 物品的體積
    :param max_weight: int - 背包的最大重量容量
    :param max_volume: int - 背包的最大體積容量
    :return: int - 能夠獲得的最大價值

    問題描述：
    給定一個重量和體積限制的背包，以及 n 個物品，每個物品有重量 weights[i]、價值 values[i] 和體積 volumes[i]。
    求能放入背包的物品的最大總價值。

    解法：
    使用動態規劃。定義 dp[w][v] 為考慮前 i 個物品，在重量限制為 w，體積限制為 v 時能達到的最大價值。
    狀態轉移方程為：
    dp[w][v] = max(dp[w][v], dp[w - weights[i-1]][v - volumes[i-1]] + values[i-1])，其中 1 <= i <= n，weights[i-1] <= w <= max_weight，volumes[i-1] <= v <= max_volume。
    """
    n = len(weights)
    dp = [[0] * (max_volume + 1) for _ in range(max_weight + 1)]

    return dp[max_weight][max_volume]


def example_knapsack_2d():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    volumes = [5, 10, 15]
    max_weight = 50
    max_volume = 20
    max_value = knapsack_2d(weights, values, volumes, max_weight, max_volume)
    print(f"二維背包問題: 最大價值為 {max_value} (預期輸出: ?)")


def knapsack_grouped(groups: List[List[Tuple[int, int]]], capacity: int) -> int:
    """
    :param groups: List[List[Tuple[int, int]]] - 每組的物品列表，每個物品用 (weight, value) 表示
    :param capacity: int - 背包的最大容量
    :return: int - 能夠獲得的最大價值

    問題描述：
    給定多組物品，每組中選擇一個物品放入背包，求能放入背包的物品的最大總價值。

    解法：
    使用動態規劃。定義 dp[w] 為背包容量為 w 時能達到的最大價值。
    對於每一組物品，對於每一個物品 (weight, value)，使用反向遍歷背包容量的方式進行動態規劃。
    """
    dp = [0] * (capacity + 1)

    return dp[capacity]


def example_knapsack_grouped():
    group1 = [(2, 10), (3, 20)]
    group2 = [(1, 15), (4, 50)]
    groups = [group1, group2]
    capacity = 5
    max_value = knapsack_grouped(groups, capacity)
    print(f"組合背包問題: 最大價值為 {max_value} (預期輸出: ?)")


def knapsack_dependent(weights: List[int], values: List[int], deps: List[List[int]], capacity: int) -> int:
    """
    :param weights: List[int] - 物品的重量
    :param values: List[int] - 物品的價值
    :param deps: List[List[int]] - 每個物品的依賴關係列表，表示物品之間的依賴性
    :param capacity: int - 背包的最大容量
    :return: int - 能夠獲得的最大價值

    問題描述：
    給定多個物品，每個物品有依賴的其他物品，只能選擇其中一部分物品放入背包，求能放入背包的物品的最大總價值。

    解法：
    使用動態規劃。將依賴背包問題轉化為 0-1 背包問題的變形，首先對依賴關係進行拓撲排序，然後按照拓撲順序進行動態規劃。
    """
    n = len(weights)
    inDegree = [0] * n
    graph = [[] for _ in range(n)]
    for i in range(n):
        for dep in deps[i]:
            graph[dep].append(i)
            inDegree[i] += 1

    dp = [0] * (capacity + 1)
    topo_order = [i for i in range(n) if inDegree[i] == 0]

    for i in topo_order:
        weight = weights[i]
        value = values[i]
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

        for j in graph[i]:
            inDegree[j] -= 1
            if inDegree[j] == 0:
                topo_order.append(j)

    return dp[capacity]


def example_dependent_knapsack():
    weights = [3, 4, 2, 1]
    values = [6, 7, 4, 1]
    dependencies = [[], [], [0], [1, 2]]
    capacity = 6
    max_value = knapsack_dependent(weights, values, dependencies, capacity)
    print(f"依賴背包問題: 最大價值為 {max_value} (預期輸出: ?)")


# 執行主函數
if __name__ == "__main__":
    example_knapsack_01()
    example_knapsack_complete()
    example_knapsack_multiple()
    # example_knapsack_fractional()
    # example_knapsack_2d()
    # example_knapsack_grouped()
    # example_dependent_knapsack()
