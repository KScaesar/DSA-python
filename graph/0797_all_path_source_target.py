import collections

from tool import debug_helper


def traversal_dfs(graph: list[list[int]]) -> list[list[int]]:
    # https://labuladong.github.io/algo/2/22/50/

    result: list[list[int]] = []
    path1 = [False] * len(graph)

    def dfs1(graph: list[list[int]], node: int):
        nonlocal result, path1

        # 環形發生
        if path1[node]:
            return

        path1[node] = True

        if node == (len(graph) - 1):
            result.append([i for i, v in enumerate(path1) if v])
            # 不需要 return, 這樣才有辦法撤銷 path1
            # 因為最後一個節點 就是終點
            # 不會執行 下方的 for range 邏輯
            #
            # 如果想要在這邊 return
            # 必須進行撤銷
            # 讓 path1[node] = False

        for child in graph[node]:
            dfs1(graph, child)

        path1[node] = False

    @debug_helper
    def dfs2(graph: list[list[int]], node: int, path: list[int]):
        nonlocal result

        # 和 backtrace 的差異
        # 進入節點才紀錄
        path.append(node)

        if node == (len(graph) - 1):
            result.append(path.copy())

        for child in graph[node]:
            dfs2(graph, child, path)

        path.pop()

    dfs1(graph, 0)
    # dfs2(graph, 0, [])
    return result


def traversal_bfs_fail(graph: list[list[int]]) -> list[list[int]]:
    result: list[list[int]] = []
    n = len(graph)
    if n == 0:
        return result

    queue = collections.deque([])
    visited = [False] * n
    path = [False] * n

    queue.append(0)
    visited[0] = True  # 防止重複進入同一個節點
    path[0] = True
    step = 0

    while len(queue) != 0:
        size = len(queue)
        print(f'path={path}, queue={queue}')

        for i in range(size):  # 把同層級的 node 都取出來, 這樣 step 才可以前進
            current = queue.popleft()

            if current == (n - 1):  # 目標條件, 通常 bfs 到達這邊, 會 return
                # bfs 無法用來找 到終點的路徑
                # path 只能使用在 dfs 概念
                #
                # 若在此函數中 查看 path
                # 只能得到多個路徑的綜合結果
                # 且 bfs 的概念 是 一層一層 往下
                # 沒有撤銷 path 的 時間點
                result.append([i for i, v in enumerate(path) if v])

            for adjacent in graph[current]:
                if not visited[adjacent]:
                    queue.append(adjacent)
                    visited[adjacent] = True
                    path[adjacent] = True

        step += 1

    return result


if __name__ == '__main__':
    sol1 = traversal_dfs([[1, 2], [3], [3], []])
    print(f'{traversal_dfs.__name__} = {sol1}')

    sol2 = traversal_dfs([[4, 3, 1], [3, 2, 4], [3], [4], []])
    print(f'{traversal_dfs.__name__} = {sol2}')

    print(traversal_bfs_fail([[1, 2], [3], [3], []]))
