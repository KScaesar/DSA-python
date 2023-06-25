package dp

import "testing"

func Test_uniquePaths(t *testing.T) {
	type args struct {
		m int
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
				m: 3,
				n: 7,
			},
			want: 28,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := uniquePaths(tt.args.m, tt.args.n); got != tt.want {
				t.Errorf("uniquePaths() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://leetcode.com/problems/unique-paths/

func uniquePaths(m int, n int) int {
	// dp[r][c] 到達 i 點 有幾種走法
	dp := make([][]int, m)
	for r := 0; r < m; r++ {
		dp[r] = make([]int, n)
		dp[r][0] = 1
	}
	for c := 0; c < n; c++ {
		dp[0][c] = 1
	}

	for r := 1; r < m; r++ {
		for c := 1; c < n; c++ {
			dp[r][c] = dp[r-1][c] + dp[r][c-1]
		}
	}
	return dp[m-1][n-1]
}
