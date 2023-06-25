package dp

import (
	"fmt"
	"testing"
)

func Test_longestCommonSubsequence(t *testing.T) {
	type args struct {
		text1 string
		text2 string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "",
			args: args{
				text1: "abcde",
				text2: "ace",
			},
			want: 3,
		},
		{
			name: "",
			args: args{
				text1: "bsbininm",
				text2: "jmjkbkjkv",
			},
			want: 1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestCommonSubsequence(tt.args.text1, tt.args.text2); got != tt.want {
				t.Errorf("longestCommonSubsequence() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://leetcode.com/problems/longest-common-subsequence/

// https://github.com/LL-Pengfei/labuladong-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.md

// https://github.com/youngyangyang04/leetcode-master/blob/master/problems/1143.%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.md

func longestCommonSubsequence(text1 string, text2 string) int {
	var max func(data ...int) int
	max = func(data ...int) int {
		ans := data[0]
		for _, n := range data {
			if ans < n {
				ans = n
			}
		}
		return ans
	}
	size1 := len(text1)
	size2 := len(text2)
	// dp[i][j] text1長度i 和 text2長度j 的最長共字串長度
	dp := make([][]int, size1+1)
	for i := 0; i < size1+1; i++ {
		dp[i] = make([]int, size2+1)
	}

	for i := 1; i < size1+1; i++ {
		for j := 1; j < size2+1; j++ {
			if text1[i-1] == text2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = max(dp[i][j-1], dp[i-1][j])
			}
		}
	}
	return dp[size1][size2]
}

func longestCommonSubsequence_fail(text1 string, text2 string) int {
	var max func(data ...int) int
	max = func(data ...int) int {
		ans := data[0]
		for _, n := range data {
			if ans < n {
				ans = n
			}
		}
		return ans
	}
	size1 := len(text1)
	size2 := len(text2)
	// dp[i][j] text1長度i 和 text2長度j 的最長共字串長度
	dp := make([][]int, size1+1)
	for i := 0; i < size1+1; i++ {
		dp[i] = make([]int, size2+1)
		dp[i][0] = 0
	}
	for j := 0; j < size2+1; j++ {
		dp[0][j] = 0
	}

	// 此方法會因為 b 對比到兩次, 但實際是text1同一個index, 對比到text2不同index
	// 0 b 4 b
	// 2 b 4 b
	// 7 m 1 m
	//
	// text1: "bsbininm",
	// text2: "jmjkbkjkv",
	for i := 1; i < size1+1; i++ {
		for j := 1; j < size2+1; j++ {
			prevMax := max(dp[i][j-1], dp[i-1][j])
			if text1[i-1] == text2[j-1] {
				fmt.Println(i-1, string(text1[i-1]), j-1, string(text2[j-1]))
				dp[i][j] = prevMax + 1
			} else {
				dp[i][j] = prevMax
			}
		}
	}
	return dp[size1][size2]
}
