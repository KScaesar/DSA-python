import collections

import tree.traversal
from tool import *


class Codec:
    # https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

    # https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-66994/dong-ge-da-d14d3/
    # 直接用分隔符號, 可能是更好的作法
    # 而不是前綴加上長度

    # 下次可以練習 遞迴 preorder 的作法 應該怎麼寫
    def serialize(self, root: TreeNode) -> str:
        if root is None:
            return ""
        queue = collections.deque([root])
        ans = []
        is_last_level = False  # 重要變數, 用來控制 只執行到最後一層節點
        while queue and not is_last_level:
            size = len(queue)
            is_last_level = True
            for _ in range(size):
                node = queue.popleft()
                if node:
                    s = str(node.val)
                    ans.append(str(len(s)))  # 加上長度, 才有辦法 decode 的時候, 解析
                    ans.append(s)
                    queue.append(node.left)
                    queue.append(node.right)

                    if node.left or node.right:
                        is_last_level = False
                else:
                    ans.append("#")

        return "".join(ans)

    def deserialize(self, data: str) -> TreeNode:
        data_size = len(data)
        root = None
        if data_size == 0:
            return root

        _len = int(data[0])
        root = TreeNode(int(data[1:1 + _len]))
        queue = collections.deque([root])
        count = _len
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()

                count += 1
                # 數字區間 [-1000, 1000]
                # 遇到 大於 10 以上的數字 or 負號
                # 只取單個字符會失效
                if count < data_size and data[count] != '#':
                    _len = int(data[count])

                    # node.left = TreeNode(int(data[count + 1:1 + _len])) # 不應該照抄 root 的作法, root 起點是 0
                    node.left = TreeNode(int(data[count + 1:count + 1 + _len]))  # 左閉右開 長度可以直接 右 - 左

                    # count += _len + 1 # 需要注意的地方
                    count += _len

                    queue.append(node.left)

                count += 1
                if count < data_size and data[count] != '#':
                    _len = int(data[count])
                    node.right = TreeNode(int(data[count + 1:count + 1 + _len]))
                    count += _len
                    queue.append(node.right)

        return root


if __name__ == '__main__':
    root1 = create_tree_by_level_order([1, 2, 3, None, None, 4, 5])
    obj = Codec()

    serialize1 = obj.serialize(root1)
    print(serialize1)

    root2 = obj.deserialize(serialize1)
    print(tree.traversal.pre_order_recursive(root2))
