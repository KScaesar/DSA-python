package dp

import (
	"fmt"
	"testing"
)

func Test_wordBreak(t *testing.T) {
	type args struct {
		s        string
		wordDict []string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "",
			args: args{
				s:        "leetcode",
				wordDict: []string{"leet", "code"},
			},
			want: true,
		},
		{
			name: "",
			args: args{
				s:        "applepenapple",
				wordDict: []string{"apple", "pen"},
			},
			want: true,
		},
		{
			name: "",
			args: args{
				s:        "dogs",
				wordDict: []string{"dog", "s", "gs"},
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := wordBreak(tt.args.s, tt.args.wordDict); got != tt.want {
				t.Errorf("wordBreak() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://leetcode.com/problems/word-break/

// dp 解法1 https://youtu.be/5_T7ihU-zdo?t=1084

// dp 解法2
// https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0139.%E5%8D%95%E8%AF%8D%E6%8B%86%E5%88%86.md

func wordBreak(s string, wordDict []string) bool {
	sizeDict := len(wordDict)
	sizeTarget := len(s)

	// dp[i][j] 是否可以產生 長度為 i 的子字串
	dp := make([]bool, sizeTarget+1)
	dp[0] = true // base case

	for i := 1; i < sizeTarget+1; i++ {
		for j := 0; j < sizeDict; j++ {
			sizeWord := len(wordDict[j])
			// 錯誤作法
			// if i-sizeWord >= 0 && s[i-sizeWord:i] == wordDict[j] {
			// 	dp[i] = dp[i-sizeWord] // 選這個字
			// 	// break
			// }

			if i-sizeWord >= 0 && s[i-sizeWord:i] == wordDict[j] && dp[i-sizeWord] {
				dp[i] = true
				break
			}
		}
	}

	// for i := 1; i < sizeTarget+1; i++ {
	// 	fmt.Println(i, string(s[i-1]), dp[i])
	// }
	return dp[sizeTarget]
}

func wordBreak_fail(s string, wordDict []string) bool {
	sizeDict := len(wordDict)
	sizeTarget := len(s)

	// dp[i][j] 用 前 j 個 dict, 是否可以產生 長度為 i 的子字串
	dp := make([][]bool, sizeTarget+1)
	for i := 0; i < sizeTarget+1; i++ {
		dp[i] = make([]bool, sizeDict+1)
	}
	for j := 0; j < sizeDict+1; j++ {
		dp[0][j] = true // base case
	}

	for i := 1; i < sizeTarget+1; i++ {
		for j := 1; j < sizeDict+1; j++ {
			sizeWord := len(wordDict[j-1])
			if i-sizeWord >= 0 && s[i-sizeWord:i] == wordDict[j-1] {
				fmt.Println(s[i-sizeWord:i], i, j)
				dp[i][j] = dp[i-sizeWord][j] // 選這個字
			} else {
				dp[i][j] = dp[i][j-1] // 不選這個字
			}
		}
	}

	for i := 1; i < sizeTarget+1; i++ {
		fmt.Println(i, string(s[i-1]), dp[i])
	}
	return dp[sizeTarget][sizeDict]
}
