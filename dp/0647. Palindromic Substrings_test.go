package dp

import "testing"

func Test_countSubstrings(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "",
			args: args{
				s: "abc",
			},
			want: 3,
		},
		{
			name: "",
			args: args{
				s: "aaa",
			},
			want: 6,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countSubstrings(tt.args.s); got != tt.want {
				t.Errorf("countSubstrings() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://leetcode.com/problems/palindromic-substrings/

// https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.md

func countSubstrings(s string) int {
	size := len(s)
	if size <= 1 {
		return size
	}

	// 	dp[l][r] 閉閉區間 s[l:r] 是否為 回文
	dp := make([][]bool, size)
	for l := 0; l < size; l++ {
		dp[l] = make([]bool, size)
	}

	cnt := 0

	for l := size - 1; l >= 0; l-- {
		for r := l; r < size; r++ {
			if r-l == 0 {
				dp[l][r] = true
			} else if r-l == 1 {
				if s[l] == s[r] {
					dp[l][r] = true
				}
			} else {
				if s[l] == s[r] {
					dp[l][r] = dp[l+1][r-1]
				}
			}

			if dp[l][r] {
				cnt++
			}
		}
	}
	return cnt
}
