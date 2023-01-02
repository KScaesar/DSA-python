import collections
from typing import List


class Solution:
    # https://www.lintcode.com/problem/178/
    # https://github.com/apachecn/apachecn-algo-zh/blob/master/docs/leetcode/python/261._Graph_Valid_Tree.md

    # 一個無向簡單圖G 滿足以下相互等價的條件之一，那麼G 是一棵樹：
    # 1. G 是沒有迴路的連通圖
    # 2, G 沒有迴路，但是在G內添加任意一條邊，就會形成一個迴路
    # 3. G 是連通的，但是如果去掉任意一條邊，就不再連通
    # 4. G內的任意兩個頂點能被唯一路徑所連通。
    # 5. 如果無向簡單圖G有n個頂點，G是連通的，有n − 1條 edge
    #
    # 對於本題而言, 可利用的是 1 和 5
    def valid_tree_v2(self, n: int, edges: List[List[int]]) -> bool:
        # 利用 union-find

        if n - 1 != len(edges):
            return False

        parent = [i for i in range(n)]
        component = n

        def find(node) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            nonlocal component
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                component -= 1

                # 錯誤作法
                # parent[node1] = root2

                # 正確作法
                parent[root1] = root2

        for n1, n2 in edges:
            if find(n1) == find(n2):
                return False
            else:
                union(n1, n2)

        return component == 0

    def valid_tree_v1(self, n: int, edges: List[List[int]]) -> bool:
        # 本題實做 寫法1

        # 寫法1
        # 利用 dfs 且 在尋訪過程 刪除鄰接節點的關係

        # 寫法2
        # 也是 dfs
        # 另外定義一个变量 prev 放到 dfs 的參數中
        # 来记录上一个结点，避免尋訪到到相鄰節點
        # https://www.cnblogs.com/grandyang/p/5257919.html

        if n - 1 != len(edges):
            return False

        _graph = collections.defaultdict(set)
        for e in edges:
            _graph[e[0]].add(e[1])
            _graph[e[1]].add(e[0])

        def dfs(_graph, cursor, visited, path) -> bool:
            if cursor in path:
                return False

            if cursor in visited:
                return True

            visited.add(cursor)
            path.add(cursor)
            # print(path)
            for child in _graph[cursor]:
                # 重點技巧:
                # 无向图边关系由节点两边共同维护，互为邻居，
                # 遍历过程需要在邻居双方共同删除关系
                # 避免迴路判斷失效
                _graph[child].remove(cursor)

                if not dfs(_graph, child, visited, path):
                    return False
            path.remove(cursor)
            return True

        # 只要滿足 tree 的條件
        # 所有節點都會滿足
        return dfs(_graph, n - 1, set(), set())

    def valid_tree_fail(self, n: int, edges: List[List[int]]) -> bool:
        # 由於鄰接節點 互相引用
        # dfs 無法判斷環形

        _graph = collections.defaultdict(list)
        for e in edges:
            # 無向圖 建構方式, 一定要兩端都加入
            _graph[e[0]].append(e[1])
            _graph[e[1]].append(e[0])

        def check(_graph, cursor, visited, path) -> bool:
            # print(cursor, path)

            # 無向圖 會同時紀錄 兩個節點的互相關系
            # 難以判斷 迴路是否存在
            if cursor in path:
                return False

            if cursor in visited:
                return True

            visited.add(cursor)
            path.add(cursor)
            for child in _graph[cursor]:
                if not check(_graph, child, visited, path):
                    return False
            path.remove(cursor)
            return True

        # print(_graph)
        return check(_graph, n - 1, set(), set())


if __name__ == '__main__':
    print("expect=True", Solution().valid_tree_v1(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print("expect=False", Solution().valid_tree_v1(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
