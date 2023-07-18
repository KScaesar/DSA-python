# https://discord.com/channels/937992003415838761/1129667911917768755/1129667911917768755
# 要求出A到B點跟C到D點在最短路徑中重複的路最多有幾個格子

# 此題不是 bfs, dfs
# 應該用數學幾何的觀念求得重疊面積
# 找這兩個長方形的交集長方形就行了，答案就是交集長方形的長加寬減ㄧ

import collections
import math


def find_all_path_bfs_fail(row: int, col: int, start: tuple[int, int], end: tuple[int, int]) -> list[list[tuple[int, int]]]:
    paths = list()
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    # matrix = [[False] * col for _ in range(row)]

    queue = collections.deque([])
    step = 0
    path = [start]
    queue.append((start, step, path))  # node, path
    visited = set(start)
    min_distance = math.inf

    while queue:
        size = len(queue)
        for _ in range(size):
            cursor, step, path = queue.popleft()
            if step > min_distance:
                continue

            if cursor == end:
                paths.append(path)
                min_distance = step
                continue

            for d_row, d_col in dirs:
                next_node = (cursor[0] + d_row, cursor[1] + d_col)
                if 0 <= next_node[0] < row and 0 <= next_node[1] < col:
                    if next_node in visited:  # 會因為找到第一個路徑後, 無法撤銷走過的路(visited), 造成找不到第二條路
                        continue
                    visited.add(next_node)

                    new_step = step + 1
                    new_path = [e for e in path]
                    new_path.append(next_node)
                    queue.append((next_node, new_step, new_path))

    return paths


def test_find_all_path_success():
    testcase = [
        (
            (4, 5, (0, 1), (3, 3)),
            [[(0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]]
        ),
        (
            (4, 5, (1, 0), (2, 4)),
            [[(1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]]
        )
    ]

    for param, expected in testcase:
        assert find_all_path_bfs_fail(*param) == expected
