package dp

import (
	"math"
	"strconv"
	"testing"
)

// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

func longestIncreasingPathV3(matrix [][]int) int {
	// 和 V2 的作法相同
	// 只是 memo 換成 array

	m := len(matrix)
	n := len(matrix[0])
	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	memo := make([][]int, len(matrix))
	for i := range memo {
		memo[i] = make([]int, len(matrix[i]))
	}

	isInside := func(row, col int) bool {
		if 0 <= row && row < m && 0 <= col && col < n {
			return true
		}
		return false
	}

	var dfs func(matrix [][]int, row, col int, prev int) int
	dfs = func(matrix [][]int, row, col int, prev int) int {
		if matrix[row][col] <= prev {
			return 0
		}

		if memo[row][col] != 0 {
			return memo[row][col]
		}

		ans := 1
		for _, d := range dirs {
			next_r, next_c := row+d[0], col+d[1]
			if !isInside(next_r, next_c) {
				continue
			}
			ans = max(ans, dfs(matrix, next_r, next_c, matrix[row][col])+1)
		}

		memo[row][col] = ans
		return ans
	}

	ans := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			ans = max(ans, dfs(matrix, r, c, math.MinInt))
		}
	}

	// println("ans =", ans)
	return ans
}

func longestIncreasingPathV2(matrix [][]int) int {
	// 利用 memo 減少子問題重複計算
	// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/solutions/2052360/python-beginner-friendly-recursion-to-dp-intuition-explained/?orderBy=most_votes

	// 重點 有回傳值的 dfs
	// base case, return 應該回傳什麼
	// 以我個人而言
	// 想使用 memo 常常想不到 有回傳值的 dfs 該怎麼寫

	m := len(matrix)
	n := len(matrix[0])
	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	memo := make(map[string]int) // k:v = position:ans
	position := func(row, col int) string {
		return strconv.Itoa(row) + "," + strconv.Itoa(col)
	}

	isInside := func(row, col int) bool {
		if 0 <= row && row < m && 0 <= col && col < n {
			return true
		}
		return false
	}

	// 不需要 path 的存在, 因為限制了要大於才能往上走
	// 所以不會走回頭路
	// 路線有方向性
	// var dfs func(matrix [][]int, row, col int, step int, path map[string]bool)

	var dfs func(matrix [][]int, row, col int, prev int) int
	dfs = func(matrix [][]int, row, col int, prev int) int {
		if matrix[row][col] <= prev {
			return 0
		}

		cursor := position(row, col)
		if v, ok := memo[cursor]; ok {
			return v
		}

		ans := 1
		for _, d := range dirs {
			next_r, next_c := row+d[0], col+d[1]
			if !isInside(next_r, next_c) {
				continue
			}
			ans = max(ans, dfs(matrix, next_r, next_c, matrix[row][col])+1)
		}

		memo[cursor] = ans
		return ans
	}

	ans := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			ans = max(ans, dfs(matrix, r, c, math.MinInt))
		}
	}

	// println("ans =", ans)
	return ans
}

func longestIncreasingPathV1(matrix [][]int) int {
	// 會出現 timeout

	m := len(matrix)
	n := len(matrix[0])
	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	ans := 0

	isInside := func(row, col int) bool {
		if 0 <= row && row < m && 0 <= col && col < n {
			return true
		}
		return false
	}
	position := func(row, col int) string {
		return strconv.Itoa(row) + "," + strconv.Itoa(col)
	}

	var dfs func(matrix [][]int, row, col int, step int, path map[string]bool)
	dfs = func(matrix [][]int, row, col int, step int, path map[string]bool) {
		cursor := position(row, col)
		if path[cursor] {
			return
		}
		path[cursor] = true

		if step > ans {
			ans = step
		}

		for _, d := range dirs {
			next_r, next_c := row+d[0], col+d[1]
			if !isInside(next_r, next_c) {
				continue
			}

			diff := int(matrix[row][col]) - int(matrix[next_r][next_c])
			// println(matrix[row][col], matrix[next_r][next_c], diff)
			if diff > 0 {
				dfs(matrix, next_r, next_c, step+1, path)
			}
		}

		path[cursor] = false
	}

	path := make(map[string]bool)
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			dfs(matrix, r, c, 1, path)
		}
	}

	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func Test_longestIncreasingPath(t *testing.T) {
	// if longestIncreasingPathV1([][]int{{9, 9, 4}, {6, 6, 8}, {2, 1, 1}}) != 4 {
	// 	t.Error("test case1 fail")
	// }
	// if longestIncreasingPathV1([][]int{{3, 4, 5}, {3, 2, 6}, {2, 2, 1}}) != 4 {
	// 	t.Error("test case2 fail")
	// }
	// if longestIncreasingPathV1([][]int{{1}}) != 1 {
	// 	t.Error("test case3 fail")
	// }

	if longestIncreasingPathV2([][]int{{9, 9, 4}, {6, 6, 8}, {2, 1, 1}}) != 4 {
		t.Error("test case1 fail")
	}
	if longestIncreasingPathV2([][]int{{3, 4, 5}, {3, 2, 6}, {2, 2, 1}}) != 4 {
		t.Error("test case2 fail")
	}
	if longestIncreasingPathV2([][]int{{1}}) != 1 {
		t.Error("test case3 fail")
	}
}
