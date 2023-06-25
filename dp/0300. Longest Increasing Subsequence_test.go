package dp

import (
	"sort"
	"testing"
)

func Test_lengthOfLIS(t *testing.T) {
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
				nums: []int{10, 9, 2, 5, 3, 7, 101, 18},
			},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := lengthOfLIS(tt.args.nums); got != tt.want {
				t.Errorf("lengthOfLIS() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://leetcode.com/problems/longest-increasing-subsequence/

// 算法筆記 p100

// https://hackmd.io/X-jeuBQaR7amGQfALM2XDQ?view#dp-%E9%99%A3%E5%88%97%E7%9A%84%E6%8A%80%E5%B7%A7

// https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0300.%E6%9C%80%E9%95%BF%E4%B8%8A%E5%8D%87%E5%AD%90%E5%BA%8F%E5%88%97.md

func lengthOfLIS(nums []int) int {
	var max func(dataAll []int) int
	max = func(dataAll []int) int {
		sort.Slice(dataAll, func(i, j int) bool {
			return dataAll[i] > dataAll[j]
		})
		return dataAll[0]
	}

	size := len(nums)
	// dp[i]: 在 nums[x~i], 以 nums[i] 為結尾, 最長遞增數值
	dp := make([]int, size)
	for i := 0; i < size; i++ {
		dp[i] = 1
	}

	for i := 1; i < size; i++ {
		for j := 0; j < i; j++ {
			if nums[i] > nums[j] {
				dp[i] = max([]int{
					dp[i],     // 以 i 元素, 重新計算
					dp[j] + 1, //
				})
			}
		}
	}
	// fmt.Println(dp)

	// 想找到整個陣列的最大值不能直接取 dp[-1], 因為定義的時候是 array[x~i]
	// 所以需要查看 dp 每個元素, 找出最大值
	return max(dp)
}
