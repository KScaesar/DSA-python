import collections


def find_order_dfs(total_course: int, prerequisites: list[list[int]]) -> list[int]:
    # Topological Sort
    # https://labuladong.github.io/algo/2/22/51/

    graph: list[list[int]] = [[] for _ in range(total_course)]
    for edge in prerequisites:
        downstream = edge[0]
        upstream = edge[1]
        graph[upstream].append(downstream)

    visited = [False] * total_course
    post_order = []
    has_cycle = False

    def traversal(start: int, path: list[bool]):
        nonlocal visited, post_order, has_cycle, graph

        if path[start]:
            has_cycle = True
            return

        if visited[start]:
            return

        visited[start] = True
        path[start] = True

        for downstream in graph[start]:
            traversal(downstream, path)

        # 后序遍历位置
        # 拓扑排序的基础是后序遍历，是因为一个任务必须等到它依赖的所有任务都完成之后才能开始开始执行
        # 后序遍历是，当左右子树的节点都被装到结果列表里面了，根节点才会被装进去。
        path[start] = False
        post_order.append(start)

    path = [False] * total_course
    for course in range(total_course):
        traversal(course, path)

    if has_cycle:
        return []
    else:
        # reversed 是 在進行 new class, 內部同時進行 reverse 動作
        # 最後回傳 reverse object, 再轉型為 list
        return list(reversed(post_order))


def find_order_bfs(total_course: int, prerequisites: list[list[int]]) -> list[int]:
    # DFS 算法利用
    # 1. path 数组判断是否存在环
    # 2. 利用逆后序遍历进行拓扑排序
    #
    # BFS 算法借助 in-degree 数组记录每个节点的「入度」，也可以实现
    # 1. 是否存在环
    # 2. 拓扑排序, 节点的bfs遍历顺序就是拓扑排序的结果

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
    result = [-1] * total_course  # 與 can finsh 不同的地方

    while len(q) != 0:
        # print(f'q={q}, in_degree={in_degree}')
        size = len(q)
        for i in range(size):
            _from = q.popleft()
            result[count] = _from  # 與 can finsh 不同的地方
            count += 1  # 記得 count++ 要放在 result[count] = _from 之後
            for _to in _graph[_from]:

                # 按道理， 图的遍历 都需要 visited 数组防止走回头路
                # 这里的 BFS 算法其实是通过 in-degree 数组实现的 visited 数组的作用
                # 只有入度为 0 的节点才能入队，从而保证不会出现死循环
                if visited[_to]:
                    continue

                in_degree[_to] -= 1
                if in_degree[_to] == 0:
                    q.append(_to)
                    visited[_to] = True

    return result if count == total_course else []


if __name__ == '__main__':
    # input1 = (2, [[1, 0], [0, 1]])
    input1 = (4, [[2, 0], [1, 0], [3, 1], [3, 2]])
    sol1 = find_order_dfs(*input1)
    print(f'{find_order_dfs.__name__} = {sol1}')

    input2 = (4, [[2, 0], [1, 0], [3, 1], [3, 2]])
    sol2 = find_order_bfs(*input2)
    print(f'{find_order_bfs.__name__} = {sol2}')
