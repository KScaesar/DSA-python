from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/path-sum/
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        # root 同時為 子葉 才滿足條件
        if targetSum - root.val == 0 and root.left is None and root.right is None:
            return True

        if targetSum < 0:
            return False

        if self.hasPathSum(root.left, targetSum - root.val):
            return True

        return self.hasPathSum(root.right, targetSum - root.val)


if __name__ == '__main__':
    print(Solution())
