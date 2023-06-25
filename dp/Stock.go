package dp

import "math"

// https://github.com/LL-Pengfei/labuladong-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%9B%A2%E7%81%AD%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98.md
// 每天都有三种「选择」：买入、卖出、无操作
//
// dp[i][k][0 or 1]
// 0 <= i <= n-1, 1 <= k <= K
// n 为天数，大 K 为最多交易数
// 此问题共 n × K × 2 种状态，全部穷举就能搞定。
//
// for 0 <= i < n:
//    for 1 <= k <= K:
//        for s in {0, 1}:
//            dp[i][k][s] = max(buy, sell, rest)

func maxProfit_greedy(prices []int) int {
	ans := 0
	min := math.MaxInt
	for i := 0; i < len(prices); i++ {
		if prices[i] < min {
			min = prices[i]
		}

		profit := prices[i] - min
		if profit > ans {
			ans = profit
		}
	}
	return ans
}

func maxProfit(prices []int) int {
	// https://programmercarl.com/0121.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA.html#%E6%80%9D%E8%B7%AF
	// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
	var maxFn func(a, b int) int
	maxFn = func(a, b int) int {
		if a < b {
			return b
		}
		return a
	}

	size := len(prices)
	// 「持有状态」: 手上有股票 or 手上沒有股票
	// 選擇: 買 或 賣
	// 持有跟買賣是不同概念

	// dp[i][0] 第i天不持有股票的最大利潤
	// dp[i][1] 第i天 持有股票的最大利潤
	dp := make([][2]int, size) // 1: 有股票, 0: 沒有股票
	dp[0][1] = -prices[0]

	// 如果第i天持有股票即dp[i][1]， 那么可以由两个状态推出来
	// 第i-1天就持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：dp[i - 1][1]
	// 第i天买入股票，所得现金就是买入今天的股票后所得现金即：-prices[i]

	// 如果第i天不持有股票即dp[i][0]， 也可以由两个状态推出来
	// 第i-1天就不持有股票，那么就保持现状，所得现金就是昨天不持有股票的所得现金 即：dp[i - 1][0]
	// 第i天卖出股票，所得现金就是按照今天股票价格卖出后所得现金即：prices[i] + dp[i - 1][1]

	for i := 1; i < size; i++ {
		dp[i][0] = maxFn(
			dp[i-1][0],           // 前一天就不持有股票, 今天保持原有狀態
			dp[i-1][1]+prices[i], // 前一天持有股票, 今天賣掉
		)
		dp[i][1] = maxFn(
			dp[i-1][1], // 前一天就持有股票, 今天保持原有狀態
			-prices[i], // 前一天不持有股票, 今天購買
			// dp[i-1][0]-prices[i], // 前一天不持有股票, 今天購買, 只能買賣一次, 所以不需要考慮之前
		)
	}
	return dp[size-1][0]
}

func maxProfitII(prices []int) int {
	// 	https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
	// 	https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html#%E6%80%9D%E8%B7%AF

	// 相關說明參考 maxProfitI

	size := len(prices)
	var maxFn func(a, b int) int
	maxFn = func(a, b int) int {
		if a < b {
			return b
		}
		return a
	}

	dp := make([][2]int, size) // 1: 有股票, 0: 沒有股票
	dp[0][1] = -prices[0]

	for i := 1; i < size; i++ {
		dp[i][0] = maxFn(
			dp[i-1][0],           // 前一天就不持有股票, 今天保持原有狀態
			dp[i-1][1]+prices[i], // 前一天持有股票, 今天賣掉
		)
		dp[i][1] = maxFn(
			dp[i-1][1], // 前一天就持有股票, 今天保持原有狀態
			// -prices[i], // 前一天不持有股票, 今天購買 ( 限制買賣一次的寫法 )
			dp[i-1][0]-prices[i], // 前一天不持有股票, 今天購買 ( 可以買賣多次)
		)
	}
	return dp[size-1][0]
}
