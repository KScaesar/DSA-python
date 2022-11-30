import collections


def can_finsh_dfs(total_course: int, prerequisites: list[list[int]]) -> bool:
    # leetcode 207
    # https://labuladong.github.io/algo/2/22/51/

    # 想以 in_degree = 0 為起點, 需要找哪些節點 不存在上游
    #
    # 後來發現 單純 dfs 尋訪 graph, 不必特別從 in_degree = 0 為起點
    # 但 in_degree 可以用來快速判斷 是否可能存在環形
    in_degree: list[int] = [0] * total_course
    graph: list[list[int]] = [[] for _ in range(total_course)]
    for edge in prerequisites:
        downstream = edge[0]
        upstream = edge[1]
        in_degree[downstream] += 1
        graph[upstream].append(downstream)

    if min(in_degree) != 0:
        return False

    # https://www.csie.ntu.edu.tw/~hsinmu/courses/_media/dsa_12spring/graph2.pdf
    # 狀態標記三色方法, 可和 path array 作對比
    # 开始时所有结点都是白色
    # 当访问过某个结点后，该结点变为灰色
    # 当该结点的所有邻接点都访问完，该节点变为黑色
    # 如果在遍历的过程中，发现某个结点有一条边指向灰色节点，并且这个灰色结点不是上一步访问的结点，那么存在环
    #
    # WHITE: 這個vertex還沒被discover
    # GRAY: 這個vertex被discover了, 但是和它相連的vertex還沒都被 discover
    # BLACK: 這個vertex及和它相連的vertex都已經被discover了
    #
    # Topological Sort
    # 每個vertex finish的時候, 就把它放到一個linked list的最前面

    visited = [False] * total_course  # 记录 traverse 曾經的路径
    path = [False] * total_course  # 记录 traverse 當下的路径
    is_cycle = False

    # dfs 只能找出 節點1 to 節點2 的所有尋訪路徑
    # 節點2 通常會設定為 結束條件所在的地方
    #
    # 但此題目要求修完所有科目, 也就是要尋訪所有節點
    # 考慮到 存在 不連通的 graph
    # 所以不可能從 dfs 單條路徑, 就判斷出是否可完成任務
    def traversal(start: int):
        nonlocal visited, graph, is_cycle

        if path[start]:
            is_cycle = True
            return

        if visited[start]:
            return

        # 前序遍历代码位置
        visited[start] = True
        path[start] = True

        for downstream in graph[start]:
            traversal(downstream)

        # 後序遍历代码位置
        path[start] = False

    # 因為眾多科目抽象成 graph
    # 不會是完整的連通圖
    # 可能各別存在獨立的 graph
    #
    # 想要修完所有科目, 就應該尋訪所有 vertex
    #
    # 图中并不是所有节点都相连
    # 所以要用一个 for 循环将所有节点都作为起点调用一次 DFS 搜索算法
    for course in range(total_course):
        traversal(course)

    # traversal 已經結束, 當下 path 當然都是 False
    print(f'{visited}\n{path}')
    return not is_cycle


def can_finsh_bfs(total_course: int, prerequisites: list[list[int]]) -> bool:
    # https://labuladong.github.io/algo/2/22/51/
    # 1. 使用邻接表 建立 _graph, 同時紀錄 每個節點 in-degree 的數值
    # 2. BFS 算法借助 in-degree 数组记录每个节点的「入度」
    # 3. 所有 in-degree = 0 的節點, 進入 queue
    # 4. 执行 BFS 循环，不断弹出队列中的节点，减少相邻节点的入度，并将入度变为 0 的节点加入队列
    # 5. 尋訪所有節點後, 若 count 等于節點數量, 则说明不存在環形

    _graph: list[list[int]] = [[] for _ in range(total_course)]
    in_degree = [0] * total_course
    for edge in prerequisites:
        _to = edge[0]
        _from = edge[1]
        _graph[_from].append(_to)
        in_degree[_to] += 1

    q = collections.deque([])
    for i in range(total_course):
        # 节点 i 没有入度，即没有依赖的节点
        if in_degree[i] == 0:
            q.append(i)

    count = 0
    visited = [False] * total_course

    while len(q) != 0:
        print(f'q={q}, in_degree={in_degree}')
        size = len(q)
        for i in range(size):
            _from = q.popleft()
            count += 1
            for _to in _graph[_from]:
                if visited[_to]:
                    continue

                in_degree[_to] -= 1
                if in_degree[_to] == 0:
                    q.append(_to)
                    visited[_to] = True

    return count == total_course


if __name__ == '__main__':
    input1 = (2, [[1, 0], [0, 1]])
    # input1 = (2, [[1, 0]])
    sol1 = can_finsh_dfs(*input1)
    print(f'{can_finsh_dfs.__name__} = {sol1}')

    input2 = (4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    sol2 = can_finsh_bfs(*input2)
    print(f'{can_finsh_bfs.__name__} = {sol2}')
