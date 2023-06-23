package dp

import (
	"fmt"
	"testing"
)

func Test_change(t *testing.T) {
	type args struct {
		amount int
		coins  []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "",
			args: args{
				amount: 5,
				coins:  []int{1, 2, 5},
			},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := change(tt.args.amount, tt.args.coins); got != tt.want {
				t.Errorf("change() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://leetcode.com/problems/coin-change-ii/

// https://discord.com/channels/937992003415838761/1120010936296685669/1121686082073931788

// https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0518.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2II.md

// https://labuladong.gitee.io/algo/di-er-zhan-a01c6/bei-bao-le-34bd4/jing-dian--70de0/

func change(amount int, coins []int) int {
	// 你要找的是，組合數，所有組成N的組合，
	// 例如 要組合成5，你有1元跟4元，
	// 如果錢放內層，你會有 1元+4元 跟 4元+1元兩種解答，
	// 但實際只需要 1個1元 + 1個4元 的一個解答

	// 放內圈代表對於每個金額都可以從頭選一次所有的硬幣
	// 你放外面，1元放完背包，往後loop，就不可能再出現1元了
	// 得到的方法数量只有{1, 4}这种情况。而不会出现{4, 1}的情况。

	// 這類的選擇問題通常為了避免重複算的情況
	// 所以會多定義一個只選擇前幾種物品的狀態
	//
	// 實際上這題的最佳解就是那種狀態再簡化而來的
	// 最原始的dp應該如下
	//
	// dp[i][j]: 用前i個硬幣, 組合 j 元有幾種方法
	// dp[i][j]=dp[i][j-coin[i]]+dp[i-1][j] (放硬幣+不放硬幣)

	// 状态有两个，就是「背包的容量」和「可选择的物品」，选择就是「装进背包」或者「不装进背包」

	size := len(coins)

	// dp[j]: 組出 j 元, 有哪幾種組合
	// dp[j]=dp[j-coin[i]]+dp[j]
	dp := make([]int, amount+1)
	dp[0] = 1

	for k := 0; k < size; k++ {
		for i := 1; i < amount+1; i++ {
			if i >= coins[k] {
				dp[i] += dp[i-coins[k]]
			}
		}
	}

	fmt.Println(dp)

	return dp[amount]
}

func change_fail(amount int, coins []int) int {
	size := len(coins)

	// dp[i]: 組出 i 元, 有哪幾種組合
	dp := make([]int, amount+1)
	dp[0] = 1

	// 求組合的話, 此作法會重複計算
	// 比如金額3
	//
	// dp[2] + 1元硬幣, 可得
	// dp[2]=[1,1]  1元 => [1,1,1]
	// dp[2]=[2]  1元 => [2,1]
	//
	// dp[1] + 2元硬幣, 可得
	// dp[1]=[1]  2元 => [1,2]
	//
	// [2,1] [1,2] 從組合的角度, 屬於同一個
	for i := 1; i < amount+1; i++ {
		for k := 0; k < size; k++ { // 進行選擇
			if i >= coins[k] {
				dp[i] += dp[i-coins[k]]
			}
		}
	}

	fmt.Println(dp)

	return dp[amount]
}
