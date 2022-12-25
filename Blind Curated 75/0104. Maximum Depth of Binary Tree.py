from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/maximum-depth-of-binary-tree/
    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def dfs(root, level):
            nonlocal depth
            if root is None:
                depth = max(depth, level)
                return

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return depth

    def maxDepth_v1(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return max(self.maxDepth_v1(root.left) + 1, self.maxDepth_v1(root.right) + 1)


if __name__ == '__main__':
    print(Solution())
