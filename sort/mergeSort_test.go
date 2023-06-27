package sort

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func mergeSort(nums []int) []int {
	// logN: 對半切陣列
	// N: merge
	// -> N*logN

	var merge func(n1, n2 []int) []int
	merge = func(n1, n2 []int) []int {
		size1 := len(n1)
		size2 := len(n2)
		if size1 == 0 {
			return n2
		} else if size2 == 0 {
			return n1
		}

		list := make([]int, 0, size1+size2)
		p1, p2 := 0, 0
		for p1 < size1 && p2 < size2 {
			if n1[p1] < n2[p2] {
				list = append(list, n1[p1])
				p1++
			} else {
				list = append(list, n2[p2])
				p2++
			}
		}

		if p1 == size1 {
			list = append(list, n2[p2:]...)
		}
		if p2 == size2 {
			list = append(list, n1[p1:]...)
		}

		return list
	}

	size := len(nums)
	// 錯誤條件
	// if size == 0 {
	// 	return nums
	// }
	if size < 2 { // 兩個以下才需要回傳
		return nums
	}

	mid := size / 2
	left := mergeSort(nums[:mid])
	right := mergeSort(nums[mid:])
	// fmt.Println(left, right)
	return merge(left, right)
}

func Test_mergeSort(t *testing.T) {
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
	}

	for _, tt := range testcase {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			actual := mergeSort(tt.params)
			assert.Equal(t, tt.expected, actual)
		})
	}

}
