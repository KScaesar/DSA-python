package graph

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

// https://leetcode.com/problems/is-graph-bipartite/

// https://web.ntnu.edu.tw/~algo/BipartiteGraph.html
// https://www.youtube.com/watch?v=lyH43SAcyjc

func isBipartite_bfs(graph [][]int) bool {
	visited := make(map[int]bool) // k:v = node:bool
	colors := make(map[int]int)   // k:v = node:color
	queue := make([]int, 0, len(graph))

	for node := range graph { // 題目說 graph 不一定連通, 所以每個節點都要尋訪
		if visited[node] { // 已尋訪
			continue
		}

		// 重點
		// bfs 是 enqueue 的時候, 紀錄是否尋訪
		// 但 level 類型的變數, 是 dequeue 的時候進行
		visited[node] = true
		queue = append(queue, node)

		color := 1 // 類似 level 變數

		for len(queue) != 0 {
			cnt := len(queue)
			for i := 0; i < cnt; i++ {
				node = queue[0]
				// fmt.Println(visited, node, color, queue)
				queue = queue[1:]
				colors[node] = color

				// 想清楚 level 類型的變數, 應該放在哪裡
				// color = -color
				for _, next := range graph[node] {
					if visited[next] {
						if colors[next] == colors[node] {
							// fmt.Printf("check: node=%v next=%v \n", node, next)
							return false
						}
						continue
					}
					visited[next] = true
					queue = append(queue, next)
				}
			}
			color = -color // 划重点：更新 color 在这里
		}
	}

	return true
}

func isBipartite_dfs(graph [][]int) bool {
	// 使用DFS以兩個顏色著色，嘗試將任意相鄰兩點塗上不同顏色
	// 如果發現有一點跟「相鄰且已經塗色的點」同一顏色，則二分圖不成立，反之成立

	memo := make(map[int]int) // k:v = node:color
	ok := true

	var dfs func(graph [][]int, cursor int, color int)
	dfs = func(graph [][]int, cursor int, color int) {
		// 注意是在節點進行 visited 判斷
		// 不要以分枝的概念, 在 for 迴圈中判斷
		// https://labuladong.github.io/algo/di-ling-zh-bfe1b/hui-su-sua-c26da/
		// https://hackmd.io/X-jeuBQaR7amGQfALM2XDQ?both#%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E5%92%8C-DFS-%E7%AE%97%E6%B3%95%E7%9A%84%E5%8C%BA%E5%88%AB
		if memo[cursor] != 0 || !ok {
			return
		}

		memo[cursor] = color // 填色, 同時有 visited 的功能

		for _, next := range graph[cursor] {
			if memo[next] != 0 && memo[next] == memo[cursor] { // 比較相鄰節點的顏色
				ok = false
				return
			}
			dfs(graph, next, -color)
		}
	}

	for node := range graph {
		dfs(graph, node, 1) // 題目說 graph 不一定連通, 所以每個節點都要尋訪
	}

	return ok
}

func Test_isBipartite(t *testing.T) {
	testcase := []struct {
		name     string
		expected bool
		params   [][]int
	}{
		{
			expected: false,
			params:   [][]int{{1, 2, 3}, {0, 2}, {0, 1, 3}, {0, 2}},
		},
		{
			expected: true,
			params:   [][]int{{1, 3}, {0, 2}, {1, 3}, {0, 2}},
		},
		{
			expected: true,
			params:   [][]int{{1, 4}, {0, 2}, {1}, {4}, {0, 3}},
		},
	}

	for _, tt := range testcase {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			assert.Equal(t, tt.expected, isBipartite_dfs(tt.params))
			assert.Equal(t, tt.expected, isBipartite_bfs(tt.params))
		})
	}
}
