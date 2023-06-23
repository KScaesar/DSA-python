package dp

import (
	"fmt"
	"math"
	"sort"
	"testing"
)

func Test_maxProduct(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "",
			args: args{
				nums: []int{2, 3, -2, 4},
			},
			want: 6,
		},
		{
			name: "",
			args: args{
				nums: []int{-2, 0, -1},
			},
			want: 0,
		},
		{
			name: "",
			args: args{
				nums: []int{1, -2, 3, -4},
			},
			want: 24,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxProduct(tt.args.nums); got != tt.want {
				t.Errorf("maxProduct() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://leetcode.com/problems/maximum-product-subarray/

// https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/152.Maximum-Product-Subarray
// 是053.Maximum-Subarray的进阶版

// https://github.com/apachecn/apachecn-algo-zh/blob/master/docs/leetcode/python/152._maximum_product_subarray.md

func maxProduct(nums []int) int {
	var max func(numbers []int) int
	max = func(numbers []int) int {
		sort.Slice(numbers, func(i, j int) bool {
			return numbers[i] > numbers[j]
		})
		return numbers[0]
	}
	var min func(numbers []int) int
	min = func(numbers []int) int {
		sort.Slice(numbers, func(i, j int) bool {
			return numbers[i] < numbers[j]
		})
		return numbers[0]
	}

	size := len(nums)
	if size == 0 {
		return 0
	}

	// 感覺類似 股票的狀態題目? 從買到賣?

	// dp[i]: 長度為 i 的子數列, 且一定包含 nums[i-1], 最大或最小相乘數值是多少
	// curMax = max( preMin*nums[i], preMax*nums[i], nums[i] );
	// curMin = min( preMin*nums[i], preMax*nums[i], nums[i] );
	dp := make([][]int, 2)
	for i := 0; i < 2; i++ {
		dp[i] = make([]int, size+1)
	}
	dp[0][0] = 1
	dp[1][0] = 1

	for k := 1; k < size+1; k++ {
		dp[0][k] = min([]int{
			dp[0][k-1] * nums[k-1], // preMinInt * num
			dp[1][k-1] * nums[k-1], // preMaxInt * num
			nums[k-1],              // 以本身為起點
		})

		dp[1][k] = max([]int{
			dp[0][k-1] * nums[k-1], // preMinInt * num
			dp[1][k-1] * nums[k-1], // preMaxInt * num
			nums[k-1],              // 以本身為起點
		})
	}

	return max(dp[1][1:]) // 長度 0 只是輔助, 不列入考慮
}

func maxProduct_fail(nums []int) int {
	var max func(v1, v2 int) int
	max = func(v1, v2 int) int {
		if v1 > v2 {
			return v1
		}
		return v2
	}

	size := len(nums)
	if size == 0 {
		return 0
	}

	// 此定義方式遇到間隔的負號, 會有錯誤, 比如: []int{1, -2, 3, -4},
	// 因为乘积可以正负正负的跳
	// dp[i]: 長度為 i 的子數列, 且一定包含 nums[i-1], 最大相乘數值是多少
	dp := make([]int, size+1)
	dp[0] = 1

	for i := 1; i < size+1; i++ {
		dp[i] = max(
			nums[i-1],         // 當前位置維新的開始
			dp[i-1]*nums[i-1], //
		)
	}

	// sol := 0 // 可能出現負號, 所以不能用 0
	sol := math.MinInt
	for i := 1; i < size+1; i++ { // 長度 0 只是輔助, 不列入考慮
		if dp[i] > sol {
			sol = dp[i]
		}
	}
	fmt.Println(dp)
	return sol
}
