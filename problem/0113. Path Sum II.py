from typing import List, Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/path-sum-ii/description/
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(root, _sum, track):
            print(_sum, track)
            if _sum == targetSum and root.left is None and root.right is None:
                ans.append(track.copy())
                return

            if root.left is not None:
                v = root.left.val
                track.append(v)
                dfs(root.left, _sum + v, track)
                track.pop()

            if root.right is not None:
                v = root.right.val
                track.append(v)
                dfs(root.right, _sum + v, track)
                track.pop()

            return

        ans = []
        if root is None:
            return ans

        dfs(root, root.val, [root.val])
        return ans


if __name__ == '__main__':
    print(Solution())
