package dp

import "testing"

// https://leetcode.com/problems/house-robber-ii/

func Test_rob_ii(t *testing.T) {
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
				nums: []int{2, 3, 2},
			},
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := rob_ii(tt.args.nums); got != tt.want {
				t.Errorf("rob() = %v, want %v", got, tt.want)
			}
		})
	}
}

// https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0213.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DII.md
// 对于一个数组，成环的话主要有如下三种情况
// 情况一：考虑不包含首尾元素
// 情况二：考虑包含首元素，不包含尾元素
// 情况三：考虑包含尾元素，不包含首元素

// https://labuladong.github.io/algo/di-er-zhan-a01c6/yong-dong--63ceb/yi-ge-fang-f3df7/

func rob_ii(nums []int) int {
	// 情況 2, 3 已經包含 情況1
	// 所以只需要比較情況 2, 3
	size := len(nums)
	if size < 2 {
		return nums[0]
	}

	select_head := nums[:size-1]
	select_tail := nums[1:size]

	sol1 := rob(select_head)
	sol2 := rob(select_tail)
	if sol1 > sol2 {
		return sol1
	}
	return sol2
}

func rob_ii_fail_v1(nums []int) int {
	size := len(nums)
	// 分成兩種情境, 比較大小
	// 1 搶了左邊界的房子
	// 2 搶了右邊界的房子

	// 會有搶到相鄰的

	rob_boundry_left := append([]int{nums[size-1]}, nums[:size-1]...)
	rob_boundry_right := append([]int{}, nums[1:]...)
	rob_boundry_right = append(rob_boundry_right, nums[0])

	ans1 := rob(rob_boundry_left)
	ans2 := rob(rob_boundry_right)
	if ans1 > ans2 {
		return ans1
	}
	return ans2
}
