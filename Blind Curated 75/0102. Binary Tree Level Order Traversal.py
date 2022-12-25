import collections
from typing import List, Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/binary-tree-level-order-traversal/
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = collections.deque([])
        q.append(root)
        ans = []

        while len(q) != 0:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)

        return ans


if __name__ == '__main__':
    print(Solution())
