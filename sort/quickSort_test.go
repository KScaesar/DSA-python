package sort

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func quickSort(nums []int) []int {
	// logN: 指每次將數組分割為兩部分的過程，也就是遞歸劃分數組的深度。
	// N: partition
	// -> N*logN

	var partition func(nums []int, start, end int) int
	partition = func(nums []int, start, end int) int {
		size := end - start + 1
		if size < 2 { // 未滿兩個不需要切分
			return start
		}

		pivotNum := nums[start]
		pivot := start
		left, right := start+1, end
		for left <= right { // 要比較的範圍, 用雙指針走訪
			if pivotNum > nums[left] {
				nums[pivot] = nums[left]
				pivot++
				left++
			} else {
				nums[left], nums[right] = nums[right], nums[left]
				right--
			}
		}
		nums[pivot] = pivotNum
		return pivot
	}

	var _quickSort func(nums []int, start, end int)
	_quickSort = func(nums []int, start, end int) {
		if end-start+1 < 2 {
			return
		}
		pivot := partition(nums, start, end)
		_quickSort(nums, start, pivot-1)
		_quickSort(nums, pivot+1, end)
	}

	_quickSort(nums, 0, len(nums)-1)
	return nums
}

func Test_quickSort(t *testing.T) {
	testcase := []struct {
		name     string
		expected []int
		params   []int
	}{
		{
			name:     "",
			expected: []int{1, 3, 3, 4, 9},
			params:   []int{4, 3, 3, 9, 1},
		},
		{
			name:     "",
			expected: []int{1, 2, 3, 4, 5, 5, 6, 7, 8, 9},
			params:   []int{5, 9, 2, 1, 4, 7, 5, 8, 3, 6},
		},
	}

	for _, tt := range testcase {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			actual := quickSort(tt.params)
			assert.Equal(t, tt.expected, actual)
		})
	}
}
