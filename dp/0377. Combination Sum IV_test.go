package dp

import (
	"fmt"
	"testing"
)

func Test_combinationSum4(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "",
			args: args{
				nums:   []int{1, 2, 3},
				target: 4,
			},
			want: 7,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := combinationSum4_dp(tt.args.nums, tt.args.target); got != tt.want {
				t.Errorf("combinationSum4() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://leetcode.com/problems/combination-sum-iv/

// dfs
// https://github.com/labuladong/fucking-algorithm/blob/master/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/%E5%AD%90%E9%9B%86%E6%8E%92%E5%88%97%E7%BB%84%E5%90%88.md

// dp
// https://programmercarl.com/0377.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C%E2%85%A3.html#%E6%80%9D%E8%B7%AF

func combinationSum4_dp(nums []int, target int) int {
	// dp[i] 目標數值i 有幾種方式可以組成
	dp := make([]int, target+1)
	dp[0] = 1

	for i := 1; i < target+1; i++ {
		for j := 0; j < len(nums); j++ {
			if i-nums[j] >= 0 {
				dp[i] += dp[i-nums[j]]
			}
		}
	}
	return dp[target]
}

func combinationSum4_dfs(nums []int, target int) int {
	size := len(nums)
	memo := make(map[int]int) // sum:cnt

	var dfs func(track []int, sum int) int
	dfs = func(track []int, sum int) int {
		if sum == target {
			fmt.Println(track)
			return 1
		} else if sum > target {
			return 0
		}

		if _, ok := memo[sum]; ok {
			return memo[sum]
		}

		// 元素可以重複選, 所以 i 每次都從0開始
		for i := 0; i < size; i++ {
			freshTrack := append(track, nums[i])
			memo[sum] += dfs(freshTrack, sum+nums[i])
		}
		return memo[sum]
	}

	return dfs([]int{}, 0)
}

func combinationSum4_dfs_timeout(nums []int, target int) int {
	size := len(nums)
	cnt := 0

	var dfs func(track []int, sum int)
	dfs = func(track []int, sum int) {
		if sum == target {
			cnt++
			return
		} else if sum > target {
			return
		}

		// 元素可以重複選, 所以 i 每次都從0開始
		for i := 0; i < size; i++ {
			freshTrack := append(track, nums[i])
			dfs(freshTrack, sum+nums[i])
		}
	}

	dfs([]int{}, 0)
	return cnt
}
