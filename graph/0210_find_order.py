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


if __name__ == '__main__':
    # input1 = (2, [[1, 0], [0, 1]])
    input1 = (4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    sol1 = find_order_dfs(*input1)
    print(f'{find_order_dfs.__name__} = {sol1}')
