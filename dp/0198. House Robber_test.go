package dp

import "testing"

// https://leetcode.com/problems/house-robber/

func Test_rob(t *testing.T) {
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
				nums: []int{1, 2, 3, 1},
			},
			want: 4,
		},
		{
			name: "",
			args: args{
				nums: []int{2, 7, 9, 3, 1},
			},
			want: 12,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := rob(tt.args.nums); got != tt.want {
				t.Errorf("rob() = %v, want %v", got, tt.want)
			}
		})
	}
}

func rob(nums []int) int {
	size := len(nums)
	// 前 i 個房子的可獲得的最大金額
	dp := make([]int, size+1)
	dp[1] = nums[0]

	for i := 2; i < size+1; i++ {
		rob_this := dp[i-2] + nums[i-1]
		not_rob_this := dp[i-1]
		if rob_this > not_rob_this {
			dp[i] = rob_this
		} else {
			dp[i] = not_rob_this
		}
	}

	return dp[size]
}
