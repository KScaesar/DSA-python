package dp

import (
	"fmt"
	"testing"
)

func Test_numDecodings(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "226",
			args: args{
				s: "226",
			},
			want: 3,
		},
		{
			name: "06",
			args: args{
				s: "06",
			},
			want: 0,
		},
		{
			// backtrack 會 timeout
			name: "111111111111111111111111111111111111111111111",
			args: args{
				s: "111111111111111111111111111111111111111111111",
			},
			want: 1836311903,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numDecodings_backtrack(tt.args.s); got != tt.want {
				t.Errorf("numDecodings_dp() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://leetcode.com/problems/decode-ways/

// https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/091.Decode-Ways

// https://github.com/halfrost/LeetCode-Go/blob/master/leetcode/0091.Decode-Ways/README.md

// https://github.com/aQuaYi/LeetCode-in-Go/blob/master/Algorithms/0091.decode-ways/decode-ways.go

func numDecodings_backtrack(s string) int {
	mapper := make(map[string]bool, 26)
	for i := 1; i <= 26; i++ {
		mapper[fmt.Sprintf("%v", i)] = true
	}

	size := len(s)
	memo := make(map[int]int, size) // cursor:cnt

	var backtrack func(cursor int) int
	backtrack = func(cursor int) int {
		if cursor == size {
			return 1
		}
		if cursor > size {
			return 0
		}

		if cnt, ok := memo[cursor]; ok {
			return cnt
		}

		one, two := 0, 0
		if mapper[s[cursor:cursor+1]] {
			one = backtrack(cursor + 1) // 取一個符號 decode
		}
		if cursor+2 <= size && mapper[s[cursor:cursor+2]] {
			two = backtrack(cursor + 2) // 取兩個符號 decode
		}

		memo[cursor] = one + two
		return memo[cursor]
	}

	return backtrack(0)
}

func numDecodings_backtrack_timeout(s string) int {
	mapper := make(map[string]bool, 26)
	for i := 1; i <= 26; i++ {
		mapper[fmt.Sprintf("%v", i)] = true
	}

	size := len(s)
	cnt := 0

	var backtrack func(cursor int, track []string)
	backtrack = func(cursor int, track []string) {
		if cursor == size {
			// fmt.Println(track)
			cnt++
			return
		}
		if cursor > size {
			return
		}

		if mapper[s[cursor:cursor+1]] {
			backtrack(cursor+1, append(track, s[cursor:cursor+1])) // 取一個符號 decode
		}
		if cursor+2 <= size && mapper[s[cursor:cursor+2]] {
			backtrack(cursor+2, append(track, s[cursor:cursor+2])) // 取兩個符號 decode
		}
	}

	backtrack(0, []string{})
	return cnt
}

func numDecodings_dp(s string) int {
	mapper := make(map[string]bool, 26)
	for i := 1; i <= 26; i++ {
		mapper[fmt.Sprintf("%v", i)] = true
	}
	// fmt.Println(mapper)

	size := len(s)

	// dp[i]: 0~i 子字串, 有幾種組合方式 ( 類似爬樓梯 leetcode 0070
	dp := make([]int, size)

	for i := 0; i < size; i++ {
		oneDecodeCount, twoDecodeCount := 0, 0
		if i == 0 {
			if mapper[s[0:1]] {
				oneDecodeCount = 1
			}
		} else if i == 1 {
			if mapper[s[0:2]] {
				twoDecodeCount = 1 // 取兩個符號 decode
			}
			if mapper[s[1:2]] {
				oneDecodeCount = dp[i-1] // 取一個符號 decode
			}
		} else {
			if mapper[s[i-1:i+1]] {
				twoDecodeCount = dp[i-2] // 取兩個符號 decode
			}
			if mapper[s[i:i+1]] {
				oneDecodeCount = dp[i-1] // 取一個符號 decode
			}
		}
		dp[i] = oneDecodeCount + twoDecodeCount
	}
	// fmt.Println(dp)
	return dp[size-1]
}
