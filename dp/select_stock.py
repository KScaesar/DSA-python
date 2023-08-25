# 宇匯知識 面試題目

def selectStock(saving: int, current: list[int], future: list[int]) -> int:
    # dp[stock][saving]
    # saving 為 w 的時候, 選擇前 0~r 個股票的最大利潤
    dp = [[0] * (saving + 1) for _ in range(len(current) + 1)]
    # 01背包如果要進行空間壓縮, 需要倒序走訪

    for r in range(1, len(current) + 1):
        stock = current[r - 1]
        for w in range(1, saving + 1):
            if w >= stock:
                dp[r][w] = max(
                    dp[r - 1][w],  # 不買這隻股票
                    dp[r - 1][w - stock] + (future[r - 1] - current[r - 1]),  # 買這隻股票
                )
            else:
                dp[r][w] = dp[r - 1][w]  # 錢不夠不買，不買就是那個狀態的最低收益

    # print(dp)
    return dp[-1][-1]


if __name__ == '__main__':
    print(selectStock(250, [175, 133, 109, 210, 97], [200, 125, 128, 228, 133]))

    # print(''.join(sorted("adfa")))
    #
    # c = 3
    # r = 5
    # print([[0] * c for _ in range(r)])
