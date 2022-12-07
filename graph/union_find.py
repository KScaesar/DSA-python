class UnionFind:
    # union-find
    # 设定树的每个节点有一个指针指向其父节点
    # 如果是根节点的话，这个指针指向自己

    # https://labuladong.github.io/algo/2/22/53/
    def __init__(self, nums: list[int] = None):
        # for v1
        if nums is None:
            self.parent: dict[int, int] = dict()
        else:
            self.parent: dict[int, int] = {num: num for num in nums}

        if nums is None:
            self.component_count = 0
        else:
            self.component_count = len(nums)

        # for v2
        # tree_total 和 find_root_with_compression 擇一使用
        # 路徑壓縮後, 就不需要 tree_total 來輔助 union 的串連方向
        if nums is None:
            self.tree_total: dict[int, int] = dict()
        else:
            self.tree_total: dict[int, int] = {num: 1 for num in nums}

        # 1. find_root 搭配 union_v2
        # 2. find_root_with_compression 搭配 union_v1

    def find_root(self, target: int) -> int:
        while self.parent[target] != target:
            target = self.parent[target]
        return target

    def find_root_with_compression(self, target: int) -> int:
        if self.parent[target] == target:
            return target

        # 背下來
        self.parent[target] = self.find_root_with_compression(self.parent[target])
        return self.parent[target]

    def union_v1(self, node1: int, node2: int):
        # O(N)
        root1 = self.find_root_with_compression(node1)
        root2 = self.find_root_with_compression(node2)
        if root1 == root2:
            return
        self.component_count -= 1
        self.parent[root1] = root2

    def union_v2(self, node1: int, node2: int):
        # O(logN)
        root1 = self.find_root(node1)
        root2 = self.find_root(node2)
        if root1 == root2:
            return

        self.component_count -= 1

        if self.tree_total[root1] > self.tree_total[root2]:
            self.parent[root2] = root1
            self.tree_total[root1] += self.tree_total[root2]
        else:
            self.parent[root1] = root2
            self.tree_total[root2] += self.tree_total[root1]

    def is_connected(self, node1, node2):
        return self.find_root_with_compression(node1) == self.find_root_with_compression(node2)

    def insert(self, num):
        if self.parent.get(num) is None:
            self.parent[num] = num


if __name__ == '__main__':
    u = UnionFind([1, 3, 4, 5, 2])
    u.union_v1(1, 2)
    print(u.is_connected(1, 3), u.is_connected(3, 5))

    u.union_v1(3, 5)
    print(u.is_connected(1, 3), u.is_connected(3, 5))

    u.union_v1(2, 3)
    print(u.is_connected(1, 3), u.is_connected(3, 5))
    print(u.component_count, u.parent)

    u = UnionFind()
    u.insert(31)
    print(u.component_count, u.parent)
