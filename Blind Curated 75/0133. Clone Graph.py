class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # https://leetcode.com/problems/clone-graph/
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        store = dict()

        def traversal(vertex) -> 'Node':
            ans = Node(val=vertex.val)
            store[vertex.val] = ans

            # print(vertex.val, [x.val for x in vertex.neighbors])
            # print('store = ', store)

            for adjacent in vertex.neighbors:
                _next = None
                if adjacent.val not in store:
                    _next = traversal(adjacent)
                else:
                    _next = store[adjacent.val]

                ans.neighbors.append(_next)

            return ans

        return traversal(node)


if __name__ == '__main__':
    print(Solution())
