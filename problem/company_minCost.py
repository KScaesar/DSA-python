import heapq


# 台積電 測驗 code1


# 在 Python 的 heap 中，可以使用元组来表示元素，
# 元组的第一个元素表示元素的大小，
# 因此可以通过比较元组的第一个元素来判断元素的大小。

# https://hackmd.io/8hGoNsKtSvKPqClgAhnJlQ#%E8%87%AA%E8%A8%82%E8%88%8A%E6%9C%89%E5%9E%8B%E5%88%A5-%E7%9A%84-compare-method
# 如果想要通过元组的第二个元素来比较元素的大小，则需要重载比较运算符。
#
# import heapq
#
# class Element:
#     def __init__(self, node, cost):
#         self.node = node
#         self.cost = cost
#
#     def __lt__(self, other):
#         return self.cost < other.cost
#
#     def __eq__(self, other):
#         return self.cost == other.cost
#
#     def __repr__(self):
#         return f"Element({self.node}, {self.cost})"
#
# heap = []
# heapq.heappush(heap, Element(2, 100))

# 本題使用 Dijkstra 算法

def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    start = initR * cols + initC
    target = finalR * cols + finalC

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    size = rows * cols
    costs = [float('inf')] * size

    costs[start] = 0
    pq = [(0, start)]  # (cost,node)
    while pq:
        state = heapq.heappop(pq)
        cost, node = state

        # 已经有一条更短的路径到达 node 节点了
        # costs 数组起到的作用就类似 visited 集合的作用。
        if cost > costs[node]:
            continue

        if node == target:
            return cost

        r, c = node // cols, node % cols
        for d in dirs:
            next_r, next_c = r + d[0], c + d[1]
            next_node = next_r * cols + next_c

            # 隱藏條件
            # costRows, costCols 可以是不同長度, 限制移動區域
            if 0 <= next_r < rows and 0 <= next_c < cols and r < len(costRows) and c < len(costCols):
                diff = 0
                if d[0] != 0:
                    diff = costRows[r]
                elif d[1] != 0:
                    diff = costCols[c]
                next_cost = cost + diff

                if costs[next_node] > next_cost:
                    costs[next_node] = next_cost
                    heapq.heappush(pq, (next_cost, next_node))
                print(f'pq={pq}', '||', costRows, costCols, f'{node}={(r, c)}', cost, '->', f'{next_node}={(next_r, next_c)}', next_cost)
        print()


if __name__ == '__main__':
    print(minCost(4, 4, 1, 0, 2, 3, [1, 2, 3], [4, 5, 6]))
