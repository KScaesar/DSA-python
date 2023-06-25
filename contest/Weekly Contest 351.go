package contest

import "fmt"

// https://leetcode.com/contest/weekly-contest-351/

// https://leetcode.com/contest/weekly-contest-351/problems/number-of-beautiful-pairs/
func countBeautifulPairs(nums []int) int {
	var first func(v int) int
	first = func(v int) int {
		for v >= 10 {
			v /= 10
		}
		return v
	}
	var last func(v int) int
	last = func(v int) int {
		return v % 10
	}
	var gcd func(v1, v2 int) int
	gcd = func(v1, v2 int) int {
		if v2 == 0 {
			return v1
		}
		return gcd(v2, v1%v2)
	}

	ans := 0
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			iv := first(nums[i])
			jv := last(nums[j])
			gcd_v := gcd(iv, jv)
			fmt.Println("i=", iv, "j=", jv, "gcd=", gcd_v)
			if gcd_v == 1 {
				ans += 1
			}
		}
	}
	return ans
}

// https://leetcode.com/contest/weekly-contest-351/problems/minimum-operations-to-make-the-integer-zero/
func makeTheIntegerZero(num1 int, num2 int) int {
	return -1
}

// https://leetcode.com/contest/weekly-contest-351/problems/ways-to-split-array-into-good-subarrays/
func numberOfGoodSubarraySplits(nums []int) int {
	return -1
}

func numberOfGoodSubarraySplits_fail(nums []int) int {
	var countFn func(nums []int, start, size int) int
	countFn = func(nums []int, start, size int) int {
		if start >= size {
			return 0
		}

		cnt := -1
		cursor := start
		for cursor < size && nums[cursor] == 0 {
			cnt++
			cursor++
		}

		if start == 0 {
			fmt.Println("start 0")
			return 1 + countFn(nums, cursor+1, size)
		}
		fmt.Println("start", cursor, "cnt", cnt)
		return cnt + countFn(nums, cursor+1, size)
	}
	return countFn(nums, 0, len(nums))
}
