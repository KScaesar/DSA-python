package dp

import (
	"fmt"
	"testing"
)

func Test_longestPalindrome(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "",
			args: args{
				s: "babad",
			},
			want: "aba",
		},
		{
			name: "",
			args: args{
				s: "cbbd",
			},
			want: "bb",
		},
		{
			name: "",
			args: args{
				s: "aacabdkacaa",
			},
			want: "aca",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestPalindrome_two_pointer(tt.args.s); got != tt.want {
				t.Errorf("longestPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://leetcode.com/problems/longest-palindromic-substring/

// 算法筆記 p386
// https://labuladong.gitee.io/algo/di-yi-zhan-da78c/shou-ba-sh-48c1d/shuang-zhi-fa4bd/

// https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0005.%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.md

func longestPalindrome_two_pointer(s string) string {
	size := len(s)
	if size == 1 {
		return s[:1]
	}

	sol := ""
	maxLen := 0

	var find_maxLen func(left, right int)
	find_maxLen = func(left, right int) {
		for i, j := left, right; i >= 0 && j < size; {
			if s[i] == s[j] {
				if j-i+1 > maxLen {
					maxLen = j - i + 1
					sol = s[i : j+1]
				}
				i--
				j++
			} else {
				break
			}
		}
	}

	for k := 0; k < size; k++ {
		find_maxLen(k, k)
		find_maxLen(k, k+1)
	}

	return sol
}

func longestPalindrome_dp(s string) string {
	size := len(s)

	// m*n 的矩陣大小
	// matrix[row][col], matrix[m][n]
	// for row in range(m):
	//    for col in range(n):
	//        matrix[row][col] = cols*i+j

	// 左閉右閉的形式
	// dp[left][right] 表示 s[left:right] 是 回文嗎?
	dp := make([][]bool, size)
	for left := 0; left < size; left++ {
		dp[left] = make([]bool, size)
	}

	maxLen := 1
	sol := s[:1]

	// 只填充右上半部分
	for left := size - 1; left >= 0; left-- {
		for right := left; right < size; right++ {
			// base case
			if left == right {
				dp[left][right] = true
				continue
			}

			if s[left] == s[right] {
				if right-1 > left+1 && left+1 >= 0 && right-1 < size {
					dp[left][right] = dp[left+1][right-1]
				} else {
					dp[left][right] = true
				}

				if dp[left][right] && right-left+1 > maxLen {
					maxLen = right - left + 1
					sol = s[left : right+1]
					fmt.Println(left, right, sol)
				}
			}
		}
	}

	return sol
}
