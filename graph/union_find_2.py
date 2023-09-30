class DSU:
    # Disjoint-Set Union

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.component_cnt = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return True  # Cycle detected

        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        elif self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_y] = parent_x
            self.rank[parent_x] += 1

        self.component_cnt -= 1
        return False  # No cycle detected


def has_cycle(edges, n):
    dsu = DSU(n)

    # 如果 edge 進行 union 發現有同樣的父節點
    # 代表出現 cycle
    # 畫圖示意會比較清楚
    for edge in edges:
        print(f'cnt={dsu.component_cnt}')
        if dsu.union(edge[0], edge[1]):
            return True

    return False


if __name__ == '__main__':
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]  # has cycle
    # edges = [(0, 1), (1, 2), (2, 3)]  # no cycle
    n = 4  # Number of nodes

    if has_cycle(edges, n):
        print("The graph contains a cycle.")
    else:
        print("The graph does not contain a cycle.")
