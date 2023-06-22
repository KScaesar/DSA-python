package dp

import "testing"

func Test_climbStairs(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "",
			args: args{
				n: 2,
			},
			want: 2,
		},
		{
			name: "",
			args: args{
				n: 3,
			},
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := climbStairs(tt.args.n); got != tt.want {
				t.Errorf("climbStairs() = %v, want %v", got, tt.want)
			}
		})
	}
}
func climbStairs(n int) int {
	// 第 i 階 有幾種走法
	dp := make([]int, n+1)

	for i := 0; i < n+1; i++ {
		if i == 0 {
			dp[i] = 1
		} else if i == 1 {
			dp[i] = 1
		} else {
			dp[i] = dp[i-1] + dp[i-2]
		}
	}
	return dp[n]
}
