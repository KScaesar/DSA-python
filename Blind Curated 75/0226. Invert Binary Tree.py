from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/invert-binary-tree/

    # 有前序 後序 兩種方法

    def invertTree_v2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # preorder

        if root is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree_v2(root.left)
        self.invertTree_v2(root.right)

        return root

    def invertTree_v1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # postorder

        if root is None:
            return None

        # 錯誤實作
        # root.right = self.invertTree(root.left)
        # root.left = self.invertTree(root.right)

        left = self.invertTree_v1(root.left)
        right = self.invertTree_v1(root.right)
        root.left = right
        root.right = left
        return root


if __name__ == '__main__':
    print(Solution())
