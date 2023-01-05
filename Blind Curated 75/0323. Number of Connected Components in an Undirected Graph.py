import collections


# https://github.com/apachecn/apachecn-algo-zh/blob/master/docs/leetcode/python/323._number_of_connected_components_in_an_undirected_graph.md
# https://ithelp.ithome.com.tw/articles/10293714


def countNumberOfConnectedComponents_dfs(n: int, edges: list[list[int]]) -> int:
    def dfs(_graph, cursor, visited):
        if cursor in visited:
            return
        visited.add(cursor)
        for node in _graph[cursor]:
            dfs(_graph, node, visited)

    _graph = collections.defaultdict(list)
    for node1, node2 in edges:
        _graph[node1].append(node2)
        _graph[node2].append(node1)

    visited = set()
    count = 0

    for node in range(n):
        if node not in visited:
            count += 1
            dfs(_graph, node, visited)

    return count


# Disjoint-set
def countNumberOfConnectedComponents_union_find(n: int, edges: list[list[int]]) -> int:
    def find(node) -> int:
        root = parent[node]
        if root != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        nonlocal component
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            component -= 1
            parent[root1] = root2

    parent = [x for x in range(n)]
    component = n

    for node1, node2 in edges:
        union(node1, node2)

    return component


if __name__ == '__main__':
    print(countNumberOfConnectedComponents_dfs(5, [[0, 1], [1, 2], [3, 4]]))
    print(countNumberOfConnectedComponents_dfs(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
    print()
    print(countNumberOfConnectedComponents_union_find(5, [[0, 1], [1, 2], [3, 4]]))
    print(countNumberOfConnectedComponents_union_find(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
