package dp

import (
	"testing"
)

func Test_coinChange(t *testing.T) {
	type args struct {
		coins  []int
		amount int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "",
			args: args{
				coins:  []int{1, 2, 5},
				amount: 11,
			},
			want: 3,
		},
		{
			name: "",
			args: args{
				coins:  []int{1},
				amount: 0,
			},
			want: 0,
		},
		{
			name: "",
			args: args{
				coins:  []int{1, 2, 5},
				amount: 100, // 用 錯誤的 bfs 作法, 容易讓 queue 佔用太多記憶體
			},
			want: 20,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := coinChange_bfs(tt.args.coins, tt.args.amount); got != tt.want {
				t.Errorf("coinChange() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://leetcode.com/problems/coin-change/

func coinChange_bfs(coins []int, amount int) int {
	q := make([]int, amount)
	visited := make(map[int]bool)

	q = append(q, 0)
	cnt := 0 // 還沒放入任何硬幣
	visited[0] = true

	for len(q) != 0 {
		size := len(q)
		for i := 0; i < size; i++ {
			current := q[0]
			q = q[1:]

			if current == amount {
				return cnt
			}

			for _, coin := range coins {
				next := current + coin
				if next > amount {
					continue
				}

				if visited[next] {
					continue
				}

				visited[next] = true
				q = append(q, next)
			}
		}
		cnt++
	}
	return -1
}

func coinChange_bfs_fail(coins []int, amount int) int {
	// 錯誤的 bfs 作法, 容易讓 queue 佔用太多記憶體

	size := len(coins)
	if size == 0 {
		return -1
	}

	if amount == 0 {
		return 0
	}

	queue := make([]int, 0, amount)
	queue = append(queue, coins...)
	level := 1 // 因為 queue 已經先放入 1 個 coin, 可以改用 -1 開始

	for len(queue) != 0 {
		cnt := len(queue)
		for i := 0; i < cnt; i++ {
			node := queue[0]
			queue = queue[1:]

			if node == amount {
				return level
			} else if node > amount {
				continue
			}

			for k := 0; k < size; k++ {
				// 可能進入同一個 node (相同的累加值)
				// 需要用 visited 防護
				queue = append(queue, coins[k]+node)
			}
		}
		level++
	}
	return -1
}

func coinChange_dp(coins []int, amount int) int {
	// https://hackmd.io/X-jeuBQaR7amGQfALM2XDQ?view#%E7%A1%AC%E5%B9%A3%E5%95%8F%E9%A1%8C

	size := len(coins)

	// dp[i]: 組出 i 元, 最少需要幾個硬幣
	dp := make([]int, amount+1)
	for i := 1; i < amount+1; i++ { // base case
		dp[i] = amount + 1 // 隨便設計一個最大值, 因為後續會進行 min 比較
	}

	for i := 1; i < amount+1; i++ {
		for k := 0; k < size; k++ { // 進行選擇
			if i >= coins[k] {
				// dp[i] = min( dp[i], dp[i-coins[k]] + 1 )
				cnt := dp[i-coins[k]] + 1
				if dp[i] > cnt {
					dp[i] = cnt
				}
			}
		}
	}
	// fmt.Println(dp)

	if dp[amount] > amount {
		return -1
	}
	return dp[amount]
}

func coinChange_fail(coins []int, amount int) int {
	// 題目是問 最少需要幾個硬幣
	// 不是問有幾種組合方式

	size := len(coins)

	// dp[i]: 組出 i 元, 有哪幾種作法
	dp := make([]int, size+1)
	dp[0] = 1

	for i := 1; i < size+1; i++ {
		for k := 0; k < size; k++ { // 進行選擇
			if i >= coins[k] {
				dp[i] += dp[i-coins[k]]
			}
		}
	}

	return dp[size]
}
